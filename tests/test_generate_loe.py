#!/usr/bin/env pytest
""" pytest tests for /app/generate_loe.py """

# Imports - Python Standard Library
from unittest.mock import patch, MagicMock

# Imports - Third-Party

# Imports - Local
import app.generate_loe

# Constants
MOCK_LOE_NAME = 'LoE - Wed May 24 00:00:00 2022.xlsx'


@patch.object(
    target=app.generate_loe,
    attribute='clear_workbook_dir'
)
def test_clear_workbook_dir(
    mock_list: MagicMock
) -> None:
    """ Test the clear_workbook_dir function.

        Args:
            mock_list (unittest.mock.MagicMock):
                Mock return object for the clear_workbook_dir function.

        Returns:
            None.
    """

    # Set the mock return value to an empty list
    mock_list.return_value = list()

    # Mock a call to the clear_workbook_dir function
    data_dir_files = app.generate_loe.clear_workbook_dir()

    # Confirm the response object to the mock function call is an empty list
    assert data_dir_files == list()


@patch.object(
    target=app.generate_loe,
    attribute='create_new_workbook'
)
def test_create_new_workbook(
    new_workbook: MagicMock
) -> None:
    """ Test the create_new_workbook function.

        Args:
            new_workbook (unittest.mock.MagicMock):
                Mock return object for the create_new_workbook
                function.

        Returns:
            None.
    """

    new_workbook.return_value = MOCK_LOE_NAME

    # Confirm the create_new_workbook function returns None
    assert app.generate_loe.create_new_workbook() == MOCK_LOE_NAME
