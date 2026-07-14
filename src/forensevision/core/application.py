"""
Clase principal de ForenseVisión.
"""

from __future__ import annotations

from forensevision.core.application_context import ApplicationContext
from forensevision.core.bootstrap import Bootstrap
from forensevision.interfaces.application_bootstrap import (
    ApplicationBootstrap,
)


class Application:
    """
    Punto de entrada programático del framework.
    """

    def __init__(
        self,
        bootstrap: ApplicationBootstrap | None = None,
    ) -> None:
        self.bootstrap: ApplicationBootstrap = (
            bootstrap
            if bootstrap is not None
            else Bootstrap()
        )

        self.context: ApplicationContext | None = None

    def initialize(self) -> None:
        """
        Inicializa la infraestructura de la aplicación.
        """

        self.context = self.bootstrap.initialize()
