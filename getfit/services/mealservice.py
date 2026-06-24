from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy.testing.pickleable import User

from getfit.dto.mealapi import AddMeal
from getfit.model.meal_model import Meals
from getfit.repository.meal_repo import MealRepository


class MealService:
    def __init__(self, repo: MealRepository):
        self.repo = repo

    def add_a_meal(self, meal: AddMeal, user_id: int):
        if not meal.meal_items:
            raise ValueError('Meal items not provided')
        total_meal =[]
        for foodname, foodamount in meal.meal_items.items():
            if foodname.strip() == "" or foodamount <= 0:
                continue
            total_meal.append(
                Meals(
                    foodname=foodname,
                    foodamount=foodamount,
                    user_id=user_id,
                    daytime=datetime.now(ZoneInfo("America/New_York"))
                )
            )
        return self.repo.create_meal(total_meal)