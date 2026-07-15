"""
Composición de pipelines del Pipeline Execution Kernel.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass

from forensevision.core.execution.step import PipelineStep


@dataclass(frozen=True, slots=True)
class Pipeline:
    """
    Define una secuencia ordenada e inmutable de pasos.
    """

    name: str
    steps: tuple[PipelineStep, ...]

    @classmethod
    def from_steps(
        cls,
        name: str,
        steps: Iterable[PipelineStep],
    ) -> Pipeline:
        """
        Construye un pipeline desde una secuencia de pasos.
        """

        return cls(
            name=name,
            steps=tuple(steps),
        )

    def __len__(self) -> int:
        """
        Obtiene el número de pasos del pipeline.
        """

        return len(self.steps)

    def __iter__(self) -> Iterator[PipelineStep]:
        """
        Itera sobre los pasos en su orden de definición.
        """

        return iter(self.steps)
