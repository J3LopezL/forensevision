"""
Contenedor de dependencias del Framework.
"""

from __future__ import annotations


class Container:
    """
    Registra servicios compartidos.
    """

    def __init__(self):

        self._services = {}

    def register(self, name: str, service):

        self._services[name] = service

    def resolve(self, name: str):

        return self._services.get(name)

    def contains(self, name: str):

        return name in self._services

    def clear(self):

        self._services.clear()
