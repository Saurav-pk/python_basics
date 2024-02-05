class Vehicle:
    color = None

def changeColor(objects, colors):
    objects.color = colors

car_1 = Vehicle()
car_2 = Vehicle()
bike = Vehicle()

changeColor(car_1, "red")
changeColor(car_2, "blue")
changeColor(bike, "black")

print(car_1.color)
print(car_2.color)
print(bike.color)

