from fastapi import FastAPI

from car import Car
from model import CarModel

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World"


@app.get("/toto")
async def root():
    return {"message": "toto"}


@app.post("/greetings/{text}")
async def copy_text(text: str):
    if text.lower() == "bonjour":
        return "Bonjour utilisateur"
    else:
        return "Utilisateur malpoli"


@app.post("/math/{number1}/{number2}")
async def copy_text(number1: int, number2: int):
    return {"result": number1 + number2}


@app.get("/car")
async def create_car():
    templateModel = CarModel("Ferrari", None)
    car = Car("Red", templateModel)
    return car
