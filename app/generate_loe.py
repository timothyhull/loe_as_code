#!/usr/bin/env python3
""" LoE generator application """

# Imports - Python Standard Library
from pathlib import Path
from os.path import join

# Imports - Third-Party
import openpyxl

# Imports - Local

# Constants
CURRENT_DIR = Path(__file__).parent
DATA_DIR = 'data'
SPREADSHEET_NAME = 'New LoE.xlsx'
SPREADSHEET_PATH = join(CURRENT_DIR, DATA_DIR, SPREADSHEET_NAME)


def create_new_workbook() -> None:
    """ Create a new Excel workbook.

        Args:
            None.

        Returns:
            None.
    """

    # Create a Workbook object
    wb = openpyxl.Workbook()

    # Add a title to the first/default worksheet
    ws = wb.active
    ws.title = 'LoE #1'

    # Save the Workbook to a file
    wb.save(
        filename=join(SPREADSHEET_PATH)
    )

    return None
