"""
Pydantic model of Compliment.
"""

from pydantic import BaseModel


class Compliment(BaseModel):
    """
    Represents a compliment response.

    Attributes:
        success (bool): The status of the response.
        data (dict): The actual data payload containing a compliment.
    """

    success: bool
    data: dict

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "success": True,
                    "data": {
                        "compliment": "Actions speak louder than words, and yours tell an incredible story."
                    },
                }
            ]
        }
    }
