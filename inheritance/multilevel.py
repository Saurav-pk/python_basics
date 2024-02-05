class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is baking")

dog = Dog()
animal = Animal()

print(animal.alive)
print(dog.alive)
animal.eat()
dog.eat()
dog.bark()