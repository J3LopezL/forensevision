"""
Sistema de configuración de ForenseVisión.
"""

from __future__ import annotations

from pathlib import Path
from typing import TypeVar, cast

import yaml

ConfigurationValue = object
T = TypeVar("T")


class Configuration:
    """
    Carga y proporciona acceso jerárquico a configuración YAML.
    """

    def __init__(self, config_path: Path) -> None:
        self._config_path = config_path
        self._data: dict[str, ConfigurationValue] = {}

    @property
    def config_path(self) -> Path:
        """
        Obtiene la ruta del archivo de configuración.
        """

        return self._config_path

    def load(self) -> None:
        """
        Carga la configuración YAML desde disco.

        Raises:
            FileNotFoundError:
                Si el archivo de configuración no existe.
            ValueError:
                Si la raíz YAML no contiene un mapping.
        """

        with self._config_path.open(
            "r",
            encoding="utf-8",
        ) as config_file:
            loaded_data = yaml.safe_load(config_file)

        if loaded_data is None:
            self._data = {}
            return

        if not isinstance(loaded_data, dict):
            raise ValueError(
                "La raíz de la configuración YAML debe ser un mapping."
            )

        self._data = cast(
            dict[str, ConfigurationValue],
            loaded_data,
        )

    def get(
        self,
        key: str,
        default: T | None = None,
    ) -> ConfigurationValue | T | None:
        """
        Obtiene un valor mediante una ruta jerárquica separada por puntos.

        Ejemplo:
            logging.level
        """

        value: ConfigurationValue = self._data

        for part in key.split("."):
            if not isinstance(value, dict):
                return default

            if part not in value:
                return default

            value = value[part]

        return value
