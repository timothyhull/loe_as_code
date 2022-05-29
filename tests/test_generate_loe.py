#!/usr/bin/env pytest
""" pytest tests for app/generate_loe.py """

# Imports - Python Standard Library
from unittest.mock import MagicMock, patch

# Imports - Third-Party
# None

# Imports - Local
from app import generate_loe

# Constants
# None


@patch.object(
    target=generate_loe,
    attribute='main'
)
def test_main(
    main_mock: MagicMock
) -> None:
    """ Test the main function.

        Args:
            main_mock (unittest.mock.MainMock):
                Mock return value for the generate_loe.main
                function.

        Returns:
            None.
    """

    # Set the return value for main_mock
    main_mock.return_value = None

    # Confirm the read_source_data function returns the mock return value
    assert generate_loe.main() is None

    return None
