"""
CLI oficial de ForenseVisión.
"""

from __future__ import annotations

import typer

from forensevision.version import __version__

app = typer.Typer(
    help="Framework ForenseVisión.",
)


@app.command()
def version():
    """
    Muestra la versión instalada.
    """
    typer.echo(f"ForenseVisión {__version__}")


@app.command()
def info():
    """
    Información general del framework.
    """
    typer.echo("Framework profesional para análisis multimedia forense.")
