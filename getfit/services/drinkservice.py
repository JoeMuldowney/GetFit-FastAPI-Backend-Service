from datetime import datetime
from zoneinfo import ZoneInfo
from getfit.dto.drinkapi import AddDrink
from getfit.model.drink_model import Drinks
from getfit.repository.drink_repo import DrinkRepository


class DrinkService:
    def __init__(self, repo: DrinkRepository):
        self.repo = repo

    def add_a_drink(self, drink: AddDrink):
        if not drink.drink_items:
            raise ValueError('Drink items not provided')
        total_drink =[]
        for drinkname, drinkamount in drink.drink_items.items():
            if drinkname.strip() == "" or drinkamount <= 0:
                continue
            total_drink.append(
                Drinks(
                    drinkname=drinkname,
                    drinkamount=drinkamount,
                    daytime=datetime.now(ZoneInfo("America/New_York"))
                )
            )
        return self.repo.create_drink(total_drink)