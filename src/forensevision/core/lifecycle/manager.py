"""
Administrador del ciclo de vida de ForenseVisión.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Final

from forensevision.core.lifecycle.exceptions import (
    InvalidLifecycleTransitionError,
    LifecycleOperationError,
)
from forensevision.core.lifecycle.state import LifecycleState
from forensevision.interfaces.lifecycle_service import (
    LifecycleService,
)


class LifecycleManager:
    """
    Controla el estado y orquesta servicios administrados.
    """

    _TRANSITIONS: Final[
        dict[LifecycleState, LifecycleState]
    ] = {
        LifecycleState.CREATED: LifecycleState.INITIALIZED,
        LifecycleState.INITIALIZED: LifecycleState.STARTING,
        LifecycleState.STARTING: LifecycleState.RUNNING,
        LifecycleState.RUNNING: LifecycleState.STOPPING,
        LifecycleState.STOPPING: LifecycleState.STOPPED,
        LifecycleState.STOPPED: LifecycleState.DISPOSED,
    }

    def __init__(self) -> None:
        self._state = LifecycleState.CREATED
        self._services: list[LifecycleService] = []

    @property
    def state(self) -> LifecycleState:
        """
        Obtiene el estado actual del ciclo de vida.
        """

        return self._state

    @property
    def services(self) -> tuple[LifecycleService, ...]:
        """
        Obtiene una vista inmutable de los servicios registrados.
        """

        return tuple(self._services)

    def register(
        self,
        service: LifecycleService,
    ) -> None:
        """
        Registra un servicio administrado.

        Raises:
            ValueError:
                Si ya existe un servicio con el mismo nombre.
        """

        if any(
            registered.name == service.name
            for registered in self._services
        ):
            raise ValueError(
                "Ya existe un servicio Lifecycle registrado "
                f"con el nombre '{service.name}'."
            )

        self._services.append(service)

    def transition_to(
        self,
        target_state: LifecycleState,
    ) -> None:
        """
        Realiza una transición al estado indicado.

        Raises:
            InvalidLifecycleTransitionError:
                Si la transición solicitada no está permitida.
        """

        expected_state = self._TRANSITIONS.get(
            self._state
        )

        if target_state is not expected_state:
            raise InvalidLifecycleTransitionError(
                current_state=self._state.value,
                target_state=target_state.value,
            )

        self._state = target_state

    def initialize(self) -> None:
        """
        Inicializa los servicios en orden de registro.
        """

        self._require_state(
            LifecycleState.CREATED
        )

        self._execute_with_compensation(
            operation="initialize",
            services=self._services,
            action=lambda service: service.initialize(),
            compensation=lambda service: service.dispose(),
        )

        self.transition_to(
            LifecycleState.INITIALIZED
        )

    def start(self) -> None:
        """
        Inicia los servicios en orden de registro.
        """

        self._require_state(
            LifecycleState.INITIALIZED
        )

        self.transition_to(
            LifecycleState.STARTING
        )

        self._execute_with_compensation(
            operation="start",
            services=self._services,
            action=lambda service: service.start(),
            compensation=lambda service: service.stop(),
        )

        self.transition_to(
            LifecycleState.RUNNING
        )

    def stop(self) -> None:
        """
        Detiene los servicios en orden inverso.
        """

        self._require_state(
            LifecycleState.RUNNING
        )

        self.transition_to(
            LifecycleState.STOPPING
        )

        self._execute(
            operation="stop",
            services=reversed(self._services),
            action=lambda service: service.stop(),
        )

        self.transition_to(
            LifecycleState.STOPPED
        )

    def dispose(self) -> None:
        """
        Libera los servicios en orden inverso.
        """

        self._require_state(
            LifecycleState.STOPPED
        )

        self._execute(
            operation="dispose",
            services=reversed(self._services),
            action=lambda service: service.dispose(),
        )

        self.transition_to(
            LifecycleState.DISPOSED
        )

    def _execute_with_compensation(
        self,
        operation: str,
        services: Iterable[LifecycleService],
        action: Callable[[LifecycleService], None],
        compensation: Callable[[LifecycleService], None],
    ) -> None:
        """
        Ejecuta una operación y compensa los servicios completados
        si se produce un fallo parcial.
        """

        completed_services: list[LifecycleService] = []

        for service in services:
            try:
                action(service)
            except Exception as error:
                self._state = LifecycleState.FAILED

                self._compensate(
                    services=reversed(completed_services),
                    compensation=compensation,
                )

                raise LifecycleOperationError(
                    operation=operation,
                    service_name=service.name,
                ) from error

            completed_services.append(service)

    def _execute(
        self,
        operation: str,
        services: Iterable[LifecycleService],
        action: Callable[[LifecycleService], None],
    ) -> None:
        """
        Ejecuta una operación Lifecycle sobre servicios administrados.
        """

        for service in services:
            try:
                action(service)
            except Exception as error:
                self._state = LifecycleState.FAILED

                raise LifecycleOperationError(
                    operation=operation,
                    service_name=service.name,
                ) from error

    def _compensate(
        self,
        services: Iterable[LifecycleService],
        compensation: Callable[[LifecycleService], None],
    ) -> None:
        """
        Ejecuta acciones compensatorias en modalidad best-effort.
        """

        for service in services:
            try:
                compensation(service)
            except Exception:
                continue

    def _require_state(
        self,
        required_state: LifecycleState,
    ) -> None:
        """
        Valida el estado requerido para una operación.
        """

        if self._state is not required_state:
            raise InvalidLifecycleTransitionError(
                current_state=self._state.value,
                target_state=required_state.value,
            )
