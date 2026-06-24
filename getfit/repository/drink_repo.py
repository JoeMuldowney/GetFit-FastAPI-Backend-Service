from sqlalchemy.orm import Session
from getfit.model.drink_model import Drinks

class DrinkRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_drink(self, drink: list[Drinks] ) -> bool:
        try:
            self.db.add_all(drink)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False