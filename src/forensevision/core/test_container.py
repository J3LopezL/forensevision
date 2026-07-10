from forensevision.core.container import Container


def test_register():

    container = Container()

    logger = object()

    container.register("logger", logger)

    assert container.resolve("logger") is logger


def test_contains():

    container = Container()

    container.register("x", object())

    assert container.contains("x")


def test_clear():

    container = Container()

    container.register("x", object())

    container.clear()

    assert not container.contains("x")
