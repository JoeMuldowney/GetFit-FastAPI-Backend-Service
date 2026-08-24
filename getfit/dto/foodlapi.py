from pydantic import BaseModel

class AddFood(BaseModel):
    food_items: dict[str, float]