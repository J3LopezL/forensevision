"""
Servicio de registro del Framework.
"""

from __future__ import annotations

import logging
from pathlib import Path


class Logger:

    """
    Configura el sistema de logging del Framework.
    """

    @staticmethod
    def configure(log_directory: Path) -> None:

        log_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)-8s | %(message)s",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler(
                    log_directory / "forensevision.log",
                    encoding="utf-8",
                ),
            ],
        )

    @staticmethod
    def get(name: str):

        return logging.getLogger(name)
