# create the hierarchy here
class Vehicle:
    ...


class WaterVehicle(Vehicle):
    ...

class Boat(WaterVehicle):
    ...

class LandVehicle(Vehicle):
    ...

class Car(LandVehicle):
    ...

class CarBoat(Car, Boat):
    ...