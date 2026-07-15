"""
Pruebas de composición del Pipeline Kernel.
"""

from forensevision.core.execution import (
    ExecutionContext,
    Pipeline,
    PipelineStep,
)


class RecordingStep(PipelineStep):
    """
    Paso mínimo utilizado para probar composición.
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
        pass


def test_pipeline_preserves_step_order() -> None:
    first = RecordingStep("first")
    second = RecordingStep("second")

    pipeline = Pipeline.from_steps(
        "evidence-analysis",
        [
            first,
            second,
        ],
    )

    assert pipeline.steps == (
        first,
        second,
    )


def test_pipeline_converts_iterable_to_tuple() -> None:
    step = RecordingStep("extract")

    pipeline = Pipeline.from_steps(
        "video-analysis",
        [step],
    )

    assert isinstance(pipeline.steps, tuple)


def test_pipeline_reports_number_of_steps() -> None:
    pipeline = Pipeline.from_steps(
        "video-analysis",
        [
            RecordingStep("extract"),
            RecordingStep("detect"),
        ],
    )

    assert len(pipeline) == 2


def test_pipeline_iterates_steps_in_definition_order() -> None:
    first = RecordingStep("first")
    second = RecordingStep("second")

    pipeline = Pipeline.from_steps(
        "evidence-analysis",
        [
            first,
            second,
        ],
    )

    assert list(pipeline) == [
        first,
        second,
    ]


def test_pipeline_accepts_empty_step_sequence() -> None:
    pipeline = Pipeline.from_steps(
        "empty",
        [],
    )

    assert len(pipeline) == 0
    assert pipeline.steps == ()
