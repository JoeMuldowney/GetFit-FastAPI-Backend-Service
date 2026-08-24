from sqlalchemy.orm import Session
from getfit.model.food_model import Foods

class FoodRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_food(self, food: list[Foods] ) -> bool:
        try:
            self.db.add_all(food)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False




