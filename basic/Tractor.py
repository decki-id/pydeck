from Car import Car

class Tractor(Car):
    def __init__(self, brand, model, year, horsepower, arms):
        super().__init__(brand, model, year, horsepower)
        self.year += 1
        self.arms = arms

    def arms(self):
        print("Arms: " + str(self.arms))

    def openTrunk(self):
        print("OPEN THE TRUNK")
        print("The trunk is opened.\n")

    def swingLeftArm(self):
        print("SWING THE LEFT ARM")
        print("The left arm is swinging.\n")