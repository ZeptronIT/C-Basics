

class car:
    def __init__(self):
        self.car_hersteller = None
        self.horse_power = None
        self.color = None
        self.x_position = 5
        self.x_position = 5
    def drive(self, x, y):
        self.x_position += x
        self.y_position += y

auto1 = car()
auto1.car_hersteller = "Bugatti"
auto1.horse_power = "1000PS"
auto1.color = "Blau"

print(auto1.car_hersteller)
print(auto1.horse_power)
print(auto1.color)

auto2 = car()
auto2.car_hersteller = "Pegani"
auto2.horse_power = "900PS"
auto2.color = "Rot"

print(auto2.car_hersteller)
print(auto2.horse_power)
print(auto2.color)


