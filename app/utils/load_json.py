"""
Function to Load JSON file
"""

import json
from json.decoder import JSONDecodeError


def load_json(file_name):
    """
    Load JSON data from the specified file.

    Args:
        file_name (str): The name of the JSON file to load.

    Returns:
        dict: The loaded JSON data.

    Raises:
        Exception: If there's an error loading the JSON file.
    """
    try:
        with open(f"app/data/{file_name}", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as exc:
        print(f"Error: JSON file '{file_name}' not found.: {exc}")
    except JSONDecodeError as err:
        print(f"Error decoding JSON file '{file_name}': {err}")
    return None
