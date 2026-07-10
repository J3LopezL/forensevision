"""
Clase principal del Framework.
"""

from __future__ import annotations

from forensevision.core.bootstrap import Bootstrap


class Application:
    """
    Punto de entrada del Framework.
    """

    def __init__(self):

        self.bootstrap = Bootstrap()

        self.context = None

    def initialize(self):

        self.context = self.bootstrap.initialize()
