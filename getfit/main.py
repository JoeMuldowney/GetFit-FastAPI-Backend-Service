from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import status

from .db.connection import get_db, engine, Base

from .repository.members_repo import PersonRepository
from .repository.meal_repo import MealRepository
from .repository.drink_repo import DrinkRepository

from .services.authservice import PersonService
from .services.mealservice import MealService
from .services.drinkservice import DrinkService
from .services.jwtservice import get_current_user, get_current_user_data

from .dto.authapi import MemberRegister, RegisterResponse, PersonFind, LoginResponse, MemberResponse
from .dto.mealapi import AddMeal
from .dto.drinkapi import AddDrink


Base.metadata.create_all(bind=engine)
app = FastAPI()

# CORS setup
origins = [
    "http://localhost:5173",  # Vite React frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_service(db: Session = Depends(get_db)):
    repo = PersonRepository(db)
    return PersonService(repo)

def get_meal_service(db: Session = Depends(get_db)):
    repo = MealRepository(db)
    return MealService(repo)

def get_drink_service(db: Session = Depends(get_db)):
    repo = DrinkRepository(db)
    return DrinkService(repo)

@app.post("/addmember", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def create_member(
        person: MemberRegister,
        service: PersonService = Depends(get_service)
):
    try:
        db_person = service.register_member(person)
        return db_person
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/findmember", response_model=LoginResponse)
def get_person(
        person: PersonFind,
        service: PersonService = Depends(get_service)

):
    try:
        return service.get_person_by_auth(person)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@app.post("/meal")
def add_meal(
        meal: AddMeal,
        user_id: int = Depends(get_current_user),
        service: MealService = Depends(get_meal_service)
):
    try:
        return service.add_a_meal(meal, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/drink")
def add_drink(
        drink: AddDrink,
        service: DrinkService = Depends(get_drink_service)
):
    try:
        return service.add_a_drink(drink)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/me", response_model=MemberResponse)
def get_me(user = Depends(get_current_user_data)):
    return user