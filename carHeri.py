from car import Car
from model import CarModel


class CarHeri(Car):
    nbOfDoor: int

    def __init__(self, nbOfDoor):
        Car.__init__(self, "red", CarModel("citroen", "tata"))
        self.nbOfDoor = nbOfDoor
