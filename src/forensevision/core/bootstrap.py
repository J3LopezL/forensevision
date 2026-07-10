"""
Inicialización del Framework.
"""

from __future__ import annotations

from forensevision.config.configuration import Configuration
from forensevision.core.paths import Paths
from forensevision.core.registry import Registry
from forensevision.logging.logger import Logger
from forensevision.interfaces.service import Service
from forensevision.core.application_context import ApplicationContext

    
class Bootstrap(Service):
    """
    Inicializa los componentes fundamentales del Framework.
    """

    @property
    def name(self) -> str:
        return "Bootstrap"

    @property
    def version(self) -> str:
        return "0.1.0"

    def __init__(self):

        self.configuration = Configuration(
            Paths.CONFIG / "default" / "application.yaml"
        )

        self.registry = Registry()

        self.logger = None

    def initialize(self):

        self.configuration.load()

        Logger.configure(Paths.LOGS)

        self.logger = Logger.get("forensevision")

        self.registry.register(
            "configuration",
            self.configuration,
        )

        self.registry.register(
            "logger",
            self.logger,
        )

        self.logger.info("Framework inicializado.")

        return ApplicationContext(
    	    configuration=self.configuration,
            registry=self.registry,
            logger=self.logger,
        )
