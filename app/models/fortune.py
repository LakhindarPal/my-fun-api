"""
Pydantic model of Fortune.
"""

from pydantic import BaseModel


class Fortune(BaseModel):
    """
    Represents a fortune response.

    Attributes:
        success (bool): The status of the response.
        data (dict): The actual data payload containing a fortune.
    """

    success: bool
    data: dict

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "success": True,
                    "data": {
                        # pylint: disable=C0301
                        "fortune": "A dream you dream alone is only a dream. A dream you dream together is reality."
                    },
                }
            ]
        }
    }
