#!/usr/bin/env pytest
""" pytest tests for /app/generate_loe.py """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from app.generate_loe import create_new_workbook


def test_create_new_workbook() -> None:
    """ Test the create_new_workbook function.

        Args:
            None.

        Returns:
            None.
    """

    assert create_new_workbook() is None
