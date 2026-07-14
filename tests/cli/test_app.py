"""
Pruebas de la CLI oficial de ForenseVisión.
"""

from typer.testing import CliRunner

from forensevision.cli.app import app
from forensevision.version import __version__

runner = CliRunner()


def test_version_command() -> None:
    result = runner.invoke(
        app,
        ["version"],
    )

    assert result.exit_code == 0
    assert (
        f"ForenseVisión {__version__}"
        in result.stdout
    )


def test_info_command() -> None:
    result = runner.invoke(
        app,
        ["info"],
    )

    assert result.exit_code == 0
    assert (
        "Framework profesional para análisis "
        "multimedia forense."
        in result.stdout
    )
