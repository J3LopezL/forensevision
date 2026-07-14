"""
Pruebas de la aplicación principal.
"""

import logging
from pathlib import Path

from forensevision.config.configuration import Configuration
from forensevision.core.application import Application
from forensevision.core.application_context import ApplicationContext
from forensevision.core.container import Container
from forensevision.core.registry import Registry


class BootstrapStub:
    """
    Bootstrap controlado para pruebas de Application.
    """

    def __init__(
        self,
        context: ApplicationContext,
    ) -> None:
        self._context = context
        self.initialize_calls = 0

    def initialize(self) -> ApplicationContext:
        self.initialize_calls += 1
        return self._context


def create_context(
    tmp_path: Path,
) -> ApplicationContext:
    configuration = Configuration(
        tmp_path / "settings.yaml"
    )

    return ApplicationContext(
        configuration=configuration,
        container=Container(),
        registry=Registry[object](),
        logger=logging.getLogger(
            "forensevision.test"
        ),
    )


def test_application_starts_without_context(
    tmp_path: Path,
) -> None:
    context = create_context(tmp_path)
    bootstrap = BootstrapStub(context)

    application = Application(
        bootstrap=bootstrap,
    )

    assert application.context is None


def test_application_initialize_stores_context(
    tmp_path: Path,
) -> None:
    context = create_context(tmp_path)
    bootstrap = BootstrapStub(context)

    application = Application(
        bootstrap=bootstrap,
    )

    application.initialize()

    assert application.context is context


def test_application_initialize_delegates_to_bootstrap(
    tmp_path: Path,
) -> None:
    context = create_context(tmp_path)
    bootstrap = BootstrapStub(context)

    application = Application(
        bootstrap=bootstrap,
    )

    application.initialize()

    assert bootstrap.initialize_calls == 1
