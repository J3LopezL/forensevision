"""
Administración centralizada de rutas del Framework.
"""

from pathlib import Path


class Paths:

    ROOT = Path(__file__).resolve().parents[3]

    SRC = ROOT / "src"

    CONFIG = ROOT / "config"

    MODELS = ROOT / "models"

    LOGS = ROOT / "logs"

    DOCS = ROOT / "docs"

    TESTS = ROOT / "tests"

    PLUGINS = ROOT / "plugins"
