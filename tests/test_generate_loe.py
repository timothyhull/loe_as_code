#!/usr/bin/env pytest
""" pytest tests for /app/generate_loe.py """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from app.generate_loe import main

# Constants


def test_main() -> None:
    """ Test the main function.

        Args:
            None.

        Returns:
            None.
    """

    # Confirm the read_source_data function returns the mock return value
    assert main() is None

    return None
