class Car:
    def __init__(self):
        self.car_hersteller = None
        self.horse_power = None
        self.color = None
        self.x_position = 5
        self.y_position = 5

    def drive(self, x, y):
        self.x_position += x
        self.y_position += y

auto1 = Car()
print(auto1.x_position)
print(auto1.y_position)
auto1.drive(5, 10)
print(auto1.x_position)
print(auto1.y_position)