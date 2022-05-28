#!/usr/bin/env python3
""" LoE generator application """

# Imports - Python Standard Library

# Imports - Third-Party

# Imports - Local
from app.loe_object import LoEObject

# Constants


def main() -> None:
    """ Main application. """

    # Create an instance of the LoEObject class
    loe = LoEObject()

    # Clear any workbook files
    # loe.clear_workbook_dir()

    # Read the source data file
    loe.read_source_data()

    # Create a new workbook file
    loe.create_new_workbook()

    # Add data to the workbook file
    loe.create_loe()

    return None


if __name__ == '__main__':
    main()
