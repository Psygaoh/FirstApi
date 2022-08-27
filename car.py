from model import CarModel


class Car:
    color: str
    model: CarModel

    def __init__(self, color, model):
        self.color = color
        self.model = model
