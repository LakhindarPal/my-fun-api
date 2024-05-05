"""
Pydantic model of PizzaIdea.
"""

from pydantic import BaseModel


class PizzaIdea(BaseModel):
    """
    Represents a pizzaidea response.

    Attributes:
        success (bool): The status of the response.
        data (dict): The actual data payload containing a pizzaidea.
    """

    success: bool
    data: dict

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "success": True,
                    "data": {
                        "pizza_idea": "BBQ Chicken Pizza with caramelized onions and bacon."
                    },
                }
            ]
        }
    }
