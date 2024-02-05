from classAndObject.car import Car

car_1 = Car("Chavy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "black")


# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)
# car_1.drive()
# car_1.stop()
# print()
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)
# car_2.drive()
# car_2.stop()

#----------------------------------Class variables-------------------------

# print(car_1.wheels)
car_1.wheels = 6
# print(car_1.wheels)
# print(car_2.wheels)
Car.wheels = 8
print(car_1.wheels)
print(car_2.wheels)