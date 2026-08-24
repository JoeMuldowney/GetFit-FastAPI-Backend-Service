from datetime import datetime
from zoneinfo import ZoneInfo

from getfit.dto.foodlapi import AddFood
from getfit.model.food_model import Foods
from getfit.repository.food_repo import FoodRepository


class FoodService:
    def __init__(self, repo: FoodRepository):
        self.repo = repo

    def add_a_food(self, food: AddFood, user_id: int):
        if not food.food_items:
            raise ValueError('fooditems not provided')
        total_food =[]
        for foodname, foodamount in food.food_items.items():
            if foodname.strip() == "" or foodamount <= 0:
                continue
            total_food.append(
                Foods(
                    foodname=foodname,
                    foodamount=foodamount,
                    user_id=user_id,
                    daytime=datetime.now(ZoneInfo("America/New_York"))
                )
            )
        return self.repo.create_food(total_food)