class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        return self.length * self.width

class Cube(Square):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        return self.length * self.width * self.height

square = Square(20,20)
print(square.area())
cube = Cube(20, 20, 20)
print(cube.area())