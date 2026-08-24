from getfit.repository.nutrition_repo import NutritionRepository

class NutritionService:
    def __init__(self, repo: NutritionRepository):
        self.repo = repo
