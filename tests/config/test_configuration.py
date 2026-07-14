"""
Pruebas del sistema de configuración.
"""

from pathlib import Path

import pytest

from forensevision.config.configuration import Configuration


def write_config(
    path: Path,
    content: str,
) -> None:
    path.write_text(
        content,
        encoding="utf-8",
    )


def test_load_and_get_nested_value(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "settings.yaml"

    write_config(
        config_path,
        """
logging:
  level: INFO
gpu:
  enabled: true
""",
    )

    configuration = Configuration(config_path)
    configuration.load()

    assert configuration.get("logging.level") == "INFO"
    assert configuration.get("gpu.enabled") is True


def test_get_returns_default_for_missing_key(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "settings.yaml"

    write_config(
        config_path,
        """
logging:
  level: INFO
""",
    )

    configuration = Configuration(config_path)
    configuration.load()

    assert configuration.get(
        "logging.format",
        "default-format",
    ) == "default-format"


def test_get_returns_default_when_path_crosses_scalar(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "settings.yaml"

    write_config(
        config_path,
        """
logging:
  level: INFO
""",
    )

    configuration = Configuration(config_path)
    configuration.load()

    assert configuration.get(
        "logging.level.value",
        "fallback",
    ) == "fallback"


def test_empty_yaml_loads_as_empty_configuration(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "settings.yaml"
    write_config(config_path, "")

    configuration = Configuration(config_path)
    configuration.load()

    assert configuration.get(
        "missing",
        "fallback",
    ) == "fallback"


def test_yaml_root_must_be_mapping(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "settings.yaml"

    write_config(
        config_path,
        """
- item-a
- item-b
""",
    )

    configuration = Configuration(config_path)

    with pytest.raises(
        ValueError,
        match="debe ser un mapping",
    ):
        configuration.load()


def test_missing_configuration_file_is_rejected(
    tmp_path: Path,
) -> None:
    configuration = Configuration(
        tmp_path / "missing.yaml"
    )

    with pytest.raises(FileNotFoundError):
        configuration.load()


def test_configuration_preserves_config_path(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "settings.yaml"

    configuration = Configuration(config_path)

    assert configuration.config_path == config_path
