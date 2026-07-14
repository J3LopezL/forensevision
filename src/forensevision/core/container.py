"""
Contenedor de dependencias de ForenseVisión.
"""

from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


class Container:
    """
    Mantiene y resuelve dependencias compartidas del framework.
    """

    def __init__(self) -> None:
        self._services: dict[str, object] = {}

    def register(
        self,
        name: str,
        service: object,
    ) -> None:
        """
        Registra una dependencia mediante su identidad lógica.
        """

        self._services[name] = service

    def resolve(
        self,
        name: str,
        service_type: type[T],
    ) -> T:
        """
        Resuelve una dependencia y valida su tipo esperado.

        Raises:
            KeyError:
                Si la dependencia no está registrada.
            TypeError:
                Si la dependencia no corresponde al tipo solicitado.
        """

        service = self._services[name]

        if not isinstance(service, service_type):
            raise TypeError(
                f"Service '{name}' is not of type "
                f"{service_type.__name__}."
            )

        return service

    def contains(self, name: str) -> bool:
        """
        Indica si una dependencia está registrada.
        """

        return name in self._services

    def clear(self) -> None:
        """
        Elimina todas las dependencias registradas.
        """

        self._services.clear()
