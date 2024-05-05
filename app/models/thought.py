"""
Pydantic model of Thought.
"""

from pydantic import BaseModel


class Thought(BaseModel):
    """
    Represents a thought response.

    Attributes:
        success (bool): The status of the response.
        data (dict): The actual data payload containing a thought.
    """

    success: bool
    data: dict

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "success": True,
                    "data": {
                        "thought": "The journey of a thousand miles begins with a single step."
                    },
                }
            ]
        }
    }
