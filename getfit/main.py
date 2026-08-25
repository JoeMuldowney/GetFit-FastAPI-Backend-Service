from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import status

from .db.connection import get_db, engine, Base

from .repository.members_repo import PersonRepository
from .repository.food_repo import FoodRepository
from .repository.drink_repo import DrinkRepository

from .services.authservice import PersonService
from .services.foodservice import FoodService
from .services.drinkservice import DrinkService
from .services.jwtservice import get_current_user, get_current_user_data

from .dto.authapi import MemberRegister, RegisterResponse, PersonFind, LoginResponse, MemberResponse
from .dto.foodlapi import AddFood
from .dto.drinkapi import AddDrink


Base.metadata.create_all(bind=engine)
app = FastAPI()

# CORS setup
origins = [
    # "http://localhost:5173",   # Local development
    "https://forgevitahq.com", # Production frontend
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

def get_service(db: Session = Depends(get_db)):
    repo = PersonRepository(db)
    return PersonService(repo)

def get_food_service(db: Session = Depends(get_db)):
    repo = FoodRepository(db)
    return FoodService(repo)

def get_drink_service(db: Session = Depends(get_db)):
    repo = DrinkRepository(db)
    return DrinkService(repo)

# Register a user
@app.post("/api/addmember", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def create_member(
        person: MemberRegister,
        service: PersonService = Depends(get_service)
):
    try:
        db_person = service.register_member(person)
        return db_person
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))


# log in a user
@app.post("/api/findmember", response_model=LoginResponse)
def get_person(
        person: PersonFind,
        service: PersonService = Depends(get_service)

):
    try:
        return service.get_person_by_auth(person)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))

# verify user
@app.get("/api/me", response_model=MemberResponse)
def get_me(user = Depends(get_current_user_data)):
    return user

@app.post("/api/food")
def add_food(
        food: AddFood,
        user_id: int = Depends(get_current_user),
        service: FoodService = Depends(get_food_service)
):
    try:
        return service.add_a_food(food, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/drink")
def add_drink(
        drink: AddDrink,
        service: DrinkService = Depends(get_drink_service)
):
    try:
        return service.add_a_drink(drink)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/daily_nutrition_intake")
def daily_nutrition_intake():
    pass