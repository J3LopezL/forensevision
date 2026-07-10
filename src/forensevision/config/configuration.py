from __future__ import annotations

from pathlib import Path

import yaml


class Configuration:
    """
    Gestiona la configuración del Framework.
    """

    def __init__(self, config_file: Path):

        self._config_file = Path(config_file)

        self._data: dict = {}

    def load(self) -> None:

        with self._config_file.open(
            "r",
            encoding="utf-8",
        ) as file:

            self._data = yaml.safe_load(file) or {}

    def get(self, key: str, default=None):
        """
        Obtiene un valor usando notación punto.

        Ejemplo:

        config.get("logging.level")
        """

        value = self._data

        for part in key.split("."):

            if not isinstance(value, dict):

                return default

            value = value.get(part)

            if value is None:

                return default

        return value
