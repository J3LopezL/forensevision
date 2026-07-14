"""
Administración centralizada de rutas de ForenseVisión.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ProjectPaths:
    """
    Representa la topología de directorios del proyecto.
    """

    root: Path

    def __init__(
        self,
        root: Path | None = None,
    ) -> None:
        resolved_root = (
            root
            if root is not None
            else Path(__file__).resolve().parents[3]
        )

        object.__setattr__(
            self,
            "root",
            resolved_root.resolve(),
        )

    @property
    def src(self) -> Path:
        """
        Obtiene el directorio de código fuente.
        """

        return self.root / "src"

    @property
    def config(self) -> Path:
        """
        Obtiene el directorio de configuración.
        """

        return self.root / "config"

    @property
    def models(self) -> Path:
        """
        Obtiene el directorio de modelos.
        """

        return self.root / "models"

    @property
    def logs(self) -> Path:
        """
        Obtiene el directorio de logs.
        """

        return self.root / "logs"

    @property
    def docs(self) -> Path:
        """
        Obtiene el directorio de documentación.
        """

        return self.root / "docs"

    @property
    def tests(self) -> Path:
        """
        Obtiene el directorio de pruebas.
        """

        return self.root / "tests"

    @property
    def plugins(self) -> Path:
        """
        Obtiene el directorio de plugins.
        """

        return self.root / "plugins"
