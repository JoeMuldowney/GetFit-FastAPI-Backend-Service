from sqlalchemy.orm import Session
from getfit.model.meal_model import Meals

class MealRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_meal(self, meal: list[Meals] ) -> bool:
        try:
            self.db.add_all(meal)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False




