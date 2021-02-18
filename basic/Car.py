# class Car
#     properties:
#         - brand
#         - model
#         - year
#         - horsepower
#     method:
#         - display info
#         - run engine
# 
# class Tractor(Car)
#     properties:
#         - arms
#     method:
#         - display info >> override
#         - open trunk
#         - swing arm


class Car():
    def __init__(self, brand, model, year, horsepower):
        self.brand = brand
        self.model = model
        self.year = year
        self.horsepower = horsepower

    def displayInfo(self):
        print("\nDISPLAY INFO")
        print("Brand: " + self.brand)
        print("Model: " + self.model)
        print("Year: " + str(self.year))
        print("Horse Power: " + self.horsepower + "\n")

    def runEngine(self):
        print("RUN ENGINE")
        print("Engine is running.\n")