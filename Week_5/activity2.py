
class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"

class Boat:
    def move(self):
        return "Sailing"

class Bicycle:
    def move(self):
        return "Cycling"
    
for vehicles in ([Car(), Plane(), Boat(), Bicycle()]):
    print(vehicles.move())