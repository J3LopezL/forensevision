"""
Contexto de ejecución del Framework.
"""

from __future__ import annotations

from dataclasses import dataclass

from forensevision.config.configuration import Configuration
from forensevision.core.registry import Registry
from logging import Logger


@dataclass
class ApplicationContext:
    """
    Contiene todos los servicios activos del Framework.
    """

    configuration: Configuration

    registry: Registry

    logger: Logger
