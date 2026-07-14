"""
Pruebas de la topología de rutas del proyecto.
"""

from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from forensevision.core.paths import ProjectPaths


def test_project_paths_preserves_resolved_root(
    tmp_path: Path,
) -> None:
    paths = ProjectPaths(tmp_path)

    assert paths.root == tmp_path.resolve()


def test_project_paths_derives_directories_from_root(
    tmp_path: Path,
) -> None:
    paths = ProjectPaths(tmp_path)

    assert paths.src == tmp_path / "src"
    assert paths.config == tmp_path / "config"
    assert paths.models == tmp_path / "models"
    assert paths.logs == tmp_path / "logs"
    assert paths.docs == tmp_path / "docs"
    assert paths.tests == tmp_path / "tests"
    assert paths.plugins == tmp_path / "plugins"


def test_project_paths_is_immutable(
    tmp_path: Path,
) -> None:
    paths = ProjectPaths(tmp_path)

    with pytest.raises(FrozenInstanceError):
        paths.root = tmp_path / "other"  # type: ignore[misc]


def test_project_paths_discovers_project_root() -> None:
    paths = ProjectPaths()

    expected_root = Path(
        __file__
    ).resolve().parents[2]

    assert paths.root == expected_root
