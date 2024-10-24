class Vehicle:
    # Class attribute
    wheels = 0

    def __init__(self, color, make, model=None):
        # Instance attributes
        self.color = color
        self.make = make
        self.model = model
        self.speed = 0

    def do_something(self):
        pass


vehicle_1 = Vehicle("Red", "Toyota", "Camry")
vehicle_2 = Vehicle("Black", "Tesla")

print(vehicle_1.color, vehicle_2.color, vehicle_1.speed)
