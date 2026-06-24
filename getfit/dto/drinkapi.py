from pydantic import BaseModel

class AddDrink(BaseModel):
    drink_items: dict[str, float]