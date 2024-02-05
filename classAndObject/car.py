class Car:

    wheels = 4

    def __init__(self, make, model, year, color):#constructor
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")