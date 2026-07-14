"""
Registro genérico de componentes de ForenseVisión.
"""

from __future__ import annotations


class Registry[T]:
    """
    Mantiene componentes identificados mediante nombres únicos.
    """

    def __init__(self) -> None:
        self._components: dict[str, T] = {}

    def register(
        self,
        name: str,
        component: T,
    ) -> None:
        """
        Registra un componente mediante su identidad lógica.
        """

        self._components[name] = component

    def get(self, name: str) -> T:
        """
        Obtiene un componente registrado.

        Raises:
            KeyError:
                Si el nombre no está registrado.
        """

        return self._components[name]

    def contains(self, name: str) -> bool:
        """
        Indica si existe un componente registrado.
        """

        return name in self._components

    def list(self) -> list[str]:
        """
        Obtiene los nombres de los componentes registrados.
        """

        return list(self._components.keys())
