from pydantic import BaseModel

class AddMeal(BaseModel):
    meal_items: dict[str, float]