from forensevision.core.execution.configuration import (
    ExecutorConfiguration,
)


def test_default_configuration_is_fail_fast() -> None:
    configuration = ExecutorConfiguration()

    assert configuration.fail_fast is True

def test_configuration_can_disable_fail_fast() -> None:
    configuration = ExecutorConfiguration(
        fail_fast=False,
    )

    assert configuration.fail_fast is False
