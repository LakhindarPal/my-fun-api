"""
Pydantic model of FunFact.
"""

from pydantic import BaseModel


class FunFact(BaseModel):
    """
    Represents a funfact response.

    Attributes:
        success (bool): The status of the response.
        data (dict): The actual data payload containing a funfact.
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
                        "fun_fact": "Did you know that the shortest war in history lasted only 38 minutes between Britain and Zanzibar in 1896?"
                    },
                }
            ]
        }
    }
