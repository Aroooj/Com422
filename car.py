class Car:
    def __init__(self, name, currentSpeed, maxSpeed, fuelLevel):
        self.name = name
        self.currentSpeed = currentSpeed
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel

    def accelerate(self, speed):
        if self.fuelLevel > 0:
            self.currentSpeed += 1
            self.fuelLevel -= 1
            if self.currentSpeed+speed > self.maxSpeed:
                print("impossible")
        else:
            self.currentSpeed = 0

    def brake(self, speed):

        if self.currentSpeed+speed > 0:
            self.currentSpeed = self.currentSpeed-1

    def refuel(self, fuel):
        if self.fuelLevel < 100:
            self.fuelLevel = self.fuelLevel+1
        else:
            self.fuelLevel = 100



