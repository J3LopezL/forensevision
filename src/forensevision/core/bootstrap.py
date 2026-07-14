"""
Inicialización de la plataforma ForenseVisión.
"""

from __future__ import annotations

from forensevision.config.configuration import Configuration
from forensevision.core.application_context import ApplicationContext
from forensevision.core.container import Container
from forensevision.core.paths import ProjectPaths
from forensevision.core.registry import Registry
from forensevision.logging.logger import ForensicLogger


class Bootstrap:
    """
    Construye las dependencias fundamentales de la aplicación.
    """

    def __init__(self) -> None:
        self.paths = ProjectPaths()

        self.configuration = Configuration(
            self.paths.config / "settings.yaml"
        )

        self.container = Container()
        self.registry: Registry[object] = Registry()

        self.forensic_logger = ForensicLogger(
            self.paths.logs
        )

    def initialize(self) -> ApplicationContext:
        """
        Inicializa la infraestructura base de la aplicación.
        """

        self.configuration.load()

        logger = self.forensic_logger.get(
            "application"
        )

        logger.info(
            "Inicializando ForenseVisión."
        )

        return ApplicationContext(
            configuration=self.configuration,
            container=self.container,
            registry=self.registry,
            logger=logger,
        )
