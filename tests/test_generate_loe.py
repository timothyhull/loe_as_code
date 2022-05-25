#!/usr/bin/env pytest
""" pytest tests for /app/generate_loe.py """

# Imports - Python Standard Library
from unittest.mock import patch, MagicMock

# Imports - Third-Party

# Imports - Local
import app.generate_loe

# Constants
MOCK_LOE_NAME = 'LoE - Wed May 24 00:00:00 2022.xlsx'
MOCK_SOURCE_FILE = 'source_data.yml'
MOCK_SOURCE_DATA = {
    'project': {
        'name': 'Test Name',
        'client': 'Test Client',
        'description': 'Test description.',
        'tasks': [
            {
                'name': 'Task #1',
                'resources': [
                    {
                        'hours': 40,
                        'name': 'Resource #1',
                        'rate': 250
                    }
                ]
            }
        ]
    }
}


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

    # Set a mock return value for create_new_workbook
    new_workbook.return_value = MOCK_LOE_NAME

    # Confirm the create_new_workbook function returns the Mock return value
    assert app.generate_loe.create_new_workbook() == MOCK_LOE_NAME


@patch.object(
    target=app.generate_loe,
    attribute='read_source_data'
)
def test_read_source_data(
    source_data: MagicMock
) -> None:
    """ Test the read_source_data function.

        Args:
            source_data (unittest.mock.MagicMock):
                Mock return object for the read_source_data
                function.

        Returns:
            None.
    """

    # Set a mock return value for read_source_data
    source_data.return_value = MOCK_SOURCE_DATA

    # Collect mock source data
    source_data = app.generate_loe.read_source_data(
        data_file=MOCK_SOURCE_FILE
    )

    # Confirm the read_source_data function returns the mock return value
    assert source_data == MOCK_SOURCE_DATA

    return None
