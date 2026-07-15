"""
Contexto tipado de una ejecución de pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from forensevision.core.execution.exceptions import (
    ContextKeyTypeConflictError,
)


@dataclass(frozen=True, slots=True)
class ContextKey[T]:
    """
    Define una clave tipada del contexto de ejecución.
    """

    name: str
    value_type: type[T]


@dataclass(slots=True)
class ExecutionContext:
    """
    Mantiene datos compartidos durante una ejecución.
    """

    _values: dict[str, object] = field(default_factory=dict)
    _types: dict[str, type[object]] = field(default_factory=dict)

    def set[T](
        self,
        key: ContextKey[T],
        value: T,
    ) -> None:
        """
        Almacena un valor asociado a una clave tipada.

        Raises:
            ContextKeyTypeConflictError:
                Si la identidad de la clave ya utiliza otro tipo.
            TypeError:
                Si el valor no corresponde al tipo de la clave.
        """

        self._validate_key_type(key)

        if not isinstance(value, key.value_type):
            raise TypeError(
                f"Context value '{key.name}' is not of type "
                f"{key.value_type.__name__}."
            )

        self._types[key.name] = key.value_type
        self._values[key.name] = value

    def get[T](
        self,
        key: ContextKey[T],
    ) -> T:
        """
        Obtiene el valor asociado a una clave tipada.

        Raises:
            KeyError:
                Si la clave no existe.
            ContextKeyTypeConflictError:
                Si la identidad de la clave utiliza otro tipo.
            TypeError:
                Si el valor almacenado no corresponde al tipo de la clave.
        """

        self._validate_key_type(key)

        value = self._values[key.name]

        if not isinstance(value, key.value_type):
            raise TypeError(
                f"Context value '{key.name}' is not of type "
                f"{key.value_type.__name__}."
            )

        return value

    def contains[T](
        self,
        key: ContextKey[T],
    ) -> bool:
        """
        Indica si una clave existe en el contexto.

        Raises:
            ContextKeyTypeConflictError:
                Si la identidad de la clave utiliza otro tipo.
        """

        self._validate_key_type(key)

        return key.name in self._values

    def _validate_key_type[T](
        self,
        key: ContextKey[T],
    ) -> None:
        registered_type = self._types.get(key.name)

        if (
            registered_type is not None
            and registered_type is not key.value_type
        ):
            raise ContextKeyTypeConflictError(
                key_name=key.name,
                registered_type=registered_type,
                requested_type=key.value_type,
            )
