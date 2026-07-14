"""
Pruebas del sistema central de logging.
"""

import logging
from pathlib import Path

from forensevision.logging.logger import ForensicLogger


def close_logger_handlers(
    logger: logging.Logger,
) -> None:
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)


def test_forensic_logger_preserves_configuration(
    tmp_path: Path,
) -> None:
    forensic_logger = ForensicLogger(
        log_directory=tmp_path,
        level=logging.DEBUG,
    )

    assert forensic_logger.log_directory == tmp_path
    assert forensic_logger.level == logging.DEBUG


def test_get_returns_standard_logger(
    tmp_path: Path,
) -> None:
    forensic_logger = ForensicLogger(tmp_path)

    logger = forensic_logger.get("pipeline")

    try:
        assert isinstance(logger, logging.Logger)
        assert logger.name == "forensevision.pipeline"
    finally:
        close_logger_handlers(logger)


def test_get_creates_log_directory(
    tmp_path: Path,
) -> None:
    log_directory = tmp_path / "logs"
    forensic_logger = ForensicLogger(log_directory)

    logger = forensic_logger.get("ocr")

    try:
        assert log_directory.is_dir()
    finally:
        close_logger_handlers(logger)


def test_logger_writes_domain_log_file(
    tmp_path: Path,
) -> None:
    forensic_logger = ForensicLogger(tmp_path)
    logger = forensic_logger.get("gpu")

    try:
        logger.info("GPU initialized")

        for handler in logger.handlers:
            handler.flush()

        log_path = tmp_path / "gpu.log"

        assert log_path.is_file()
        assert "GPU initialized" in log_path.read_text(
            encoding="utf-8"
        )
    finally:
        close_logger_handlers(logger)


def test_get_does_not_duplicate_handlers(
    tmp_path: Path,
) -> None:
    forensic_logger = ForensicLogger(tmp_path)

    first_logger = forensic_logger.get("detectors")
    second_logger = forensic_logger.get("detectors")

    try:
        assert first_logger is second_logger
        assert len(first_logger.handlers) == 1
    finally:
        close_logger_handlers(first_logger)


def test_logger_does_not_propagate_to_root(
    tmp_path: Path,
) -> None:
    forensic_logger = ForensicLogger(tmp_path)

    logger = forensic_logger.get("errors")

    try:
        assert logger.propagate is False
    finally:
        close_logger_handlers(logger)
