"""
Function to Get Random Item
"""

import random
from fastapi import HTTPException


def get_random(data):
    """
    Get a random item from the provided data.

    Args:
        data (list): The list of items to choose from.

    Returns:
        Any: A random item from the provided data.

    Raises:
        HTTPException: If the provided data is empty.
    """
    if not data:
        raise HTTPException(status_code=404, detail=f"No {data.__name__} is found.")

    return random.choice(data)
