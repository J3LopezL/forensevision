"""
Pruebas del ejecutor secuencial del Pipeline Kernel.
"""

from forensevision.core.execution import (
    ContextKey,
    ExecutionContext,
    Pipeline,
    PipelineStep,
    SequentialExecutor,
    StepStatus,
)


class ExecutedSteps(list[str]):
    """
    Colección nominal de pasos ejecutados.
    """


EXECUTED_STEPS = ContextKey[ExecutedSteps](
    name="executed_steps",
    value_type=ExecutedSteps,
)


class RecordingStep(PipelineStep):
    """
    Paso que registra su nombre en el contexto.
    """

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        executed = context.get(EXECUTED_STEPS)
        executed.append(self.name)


class FailingStep(PipelineStep):
    """
    Paso que produce un fallo controlado.
    """

    @property
    def name(self) -> str:
        return "failing"

    def execute(
        self,
        context: ExecutionContext,
    ) -> None:
        raise RuntimeError("step failure")


def test_executor_runs_steps_in_pipeline_order() -> None:
    context = ExecutionContext()
    context.set(
        EXECUTED_STEPS,
        ExecutedSteps(),
    )

    pipeline = Pipeline.from_steps(
        "ordered",
        [
            RecordingStep("first"),
            RecordingStep("second"),
            RecordingStep("third"),
        ],
    )

    result = SequentialExecutor().execute(
        pipeline,
        context,
    )

    assert context.get(EXECUTED_STEPS) == [
        "first",
        "second",
        "third",
    ]
    assert result.succeeded is True


def test_executor_builds_succeeded_results() -> None:
    context = ExecutionContext()
    context.set(
        EXECUTED_STEPS,
        ExecutedSteps(),
    )

    pipeline = Pipeline.from_steps(
        "success",
        [
            RecordingStep("extract"),
            RecordingStep("detect"),
        ],
    )

    result = SequentialExecutor().execute(
        pipeline,
        context,
    )

    assert [
        step.status
        for step in result.steps
    ] == [
        StepStatus.SUCCEEDED,
        StepStatus.SUCCEEDED,
    ]


def test_executor_stops_execution_after_failure() -> None:
    context = ExecutionContext()
    context.set(
        EXECUTED_STEPS,
        ExecutedSteps(),
    )

    pipeline = Pipeline.from_steps(
        "fail-fast",
        [
            RecordingStep("first"),
            FailingStep(),
            RecordingStep("never-executed"),
        ],
    )

    result = SequentialExecutor().execute(
        pipeline,
        context,
    )

    assert context.get(EXECUTED_STEPS) == [
        "first",
    ]
    assert [
        step.status
        for step in result.steps
    ] == [
        StepStatus.SUCCEEDED,
        StepStatus.FAILED,
        StepStatus.SKIPPED,
    ]


def test_executor_preserves_original_exception() -> None:
    context = ExecutionContext()

    pipeline = Pipeline.from_steps(
        "failure",
        [
            FailingStep(),
        ],
    )

    result = SequentialExecutor().execute(
        pipeline,
        context,
    )

    error = result.steps[0].error

    assert isinstance(error, RuntimeError)
    assert str(error) == "step failure"


def test_executor_handles_empty_pipeline() -> None:
    context = ExecutionContext()

    pipeline = Pipeline.from_steps(
        "empty",
        [],
    )

    result = SequentialExecutor().execute(
        pipeline,
        context,
    )

    assert result.steps == ()
    assert result.succeeded is True
    assert result.failed is False
