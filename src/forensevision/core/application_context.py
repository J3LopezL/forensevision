"""
Contexto de ejecución de ForenseVisión.
"""

from __future__ import annotations

import logging

from forensevision.config.configuration import Configuration
from forensevision.core.container import Container
from forensevision.core.registry import Registry


class ApplicationContext:
    """
    Agrupa las dependencias fundamentales de la aplicación.
    """

    def __init__(
        self,
        configuration: Configuration,
        container: Container,
        registry: Registry[object],
        logger: logging.Logger,
    ) -> None:
        self.configuration = configuration
        self.container = container
        self.registry = registry
        self.logger = logger
