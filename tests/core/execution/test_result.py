"""
Pruebas de resultados de ejecución.
"""

from forensevision.core.execution import (
    PipelineResult,
    StepResult,
    StepStatus,
)


def test_step_result_builds_succeeded_result() -> None:
    result = StepResult.succeeded("extract_frames")

    assert result.step_name == "extract_frames"
    assert result.status is StepStatus.SUCCEEDED
    assert result.error is None


def test_step_result_builds_failed_result() -> None:
    error = RuntimeError("decoder failure")

    result = StepResult.failed(
        "decode_video",
        error,
    )

    assert result.step_name == "decode_video"
    assert result.status is StepStatus.FAILED
    assert result.error is error


def test_step_result_builds_skipped_result() -> None:
    result = StepResult.skipped("detect_faces")

    assert result.status is StepStatus.SKIPPED
    assert result.error is None


def test_empty_pipeline_result_is_succeeded() -> None:
    result = PipelineResult()

    assert result.succeeded is True
    assert result.failed is False


def test_pipeline_result_succeeds_when_all_steps_succeed() -> None:
    result = PipelineResult(
        steps=(
            StepResult.succeeded("extract"),
            StepResult.succeeded("detect"),
        )
    )

    assert result.succeeded is True
    assert result.failed is False


def test_pipeline_result_fails_when_step_fails() -> None:
    result = PipelineResult(
        steps=(
            StepResult.succeeded("extract"),
            StepResult.failed(
                "detect",
                RuntimeError("detection failure"),
            ),
        )
    )

    assert result.succeeded is False
    assert result.failed is True


def test_pipeline_result_is_not_succeeded_when_step_is_skipped() -> None:
    result = PipelineResult(
        steps=(
            StepResult.succeeded("extract"),
            StepResult.skipped("detect"),
        )
    )

    assert result.succeeded is False
    assert result.failed is False
