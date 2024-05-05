"""
Pydantic model of LifeTruth.
"""

from pydantic import BaseModel


class LifeTruth(BaseModel):
    """
    Represents a lifetruth response.

    Attributes:
        success (bool): The status of the response.
        data (dict): The actual data payload containing a lifetruth.
    """

    success: bool
    data: dict

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "success": True,
                    "data": {"life_truth": "The only constant in life is change."},
                }
            ]
        }
    }
