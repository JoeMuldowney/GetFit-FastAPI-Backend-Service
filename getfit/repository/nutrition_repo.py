from sqlalchemy.orm import Session

class NutritionRepository:
    def __init__(self, db: Session):
        self.db = db