from forensevision.core.registry import Registry


def test_registry_register():

    registry = Registry()

    registry.register(
        "logger",
        object(),
    )

    assert registry.contains("logger")


def test_registry_get():

    registry = Registry()

    logger = object()

    registry.register(
        "logger",
        logger,
    )

    assert registry.get("logger") is logger


def test_registry_list():

    registry = Registry()

    registry.register("b", object())

    registry.register("a", object())

    assert registry.list() == ["a", "b"]

