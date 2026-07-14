"""
Sistema central de logging de ForenseVisión.
"""

from __future__ import annotations

import logging
from pathlib import Path


class ForensicLogger:
    """
    Fábrica central de loggers del framework.
    """

    _FORMAT = (
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(message)s"
    )

    def __init__(
        self,
        log_directory: Path,
        level: int = logging.INFO,
    ) -> None:
        self._log_directory = log_directory
        self._level = level

    @property
    def log_directory(self) -> Path:
        """
        Obtiene el directorio configurado para logs.
        """

        return self._log_directory

    @property
    def level(self) -> int:
        """
        Obtiene el nivel de logging configurado.
        """

        return self._level

    def get(self, name: str) -> logging.Logger:
        """
        Obtiene un logger configurado para un dominio lógico.
        """

        self._log_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        logger = logging.getLogger(
            f"forensevision.{name}"
        )

        logger.setLevel(self._level)
        logger.propagate = False

        if not logger.handlers:
            handler = logging.FileHandler(
                self._log_directory / f"{name}.log",
                encoding="utf-8",
            )

            handler.setLevel(self._level)
            handler.setFormatter(
                logging.Formatter(self._FORMAT)
            )

            logger.addHandler(handler)

        return logger
