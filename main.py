from car import Car


c_one = Car("Fiat", 50, 110, 0)
c_two = Car("Hyundai", 70, 120, 80)


print(f"{c_one.name} is driving at the speed of {c_one.currentSpeed}")
print(f"{c_one.name} and {c_two.name} have the max speed of {c_one.maxSpeed} and {c_two.maxSpeed}")
print(f"And their fuel levels are {c_one.fuelLevel} and {c_two.fuelLevel}, respectively")

Car.accelerate(c_one, 120)
Car.accelerate(c_two, 130)
Car.accelerate(c_one, 50)
Car.brake(c_one, 5)
