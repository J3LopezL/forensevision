"""
Registro central de componentes del Framework.
"""

from __future__ import annotations


class Registry:
    """
    Mantiene registrados los componentes disponibles.
    """

    def __init__(self):

        self._components = {}

    def register(self, name: str, component):

        self._components[name] = component

    def get(self, name: str):

        return self._components.get(name)

    def contains(self, name: str):

        return name in self._components

    def list(self):

        return sorted(self._components.keys())
