class Pray:
    def flee(self):
        print("This animal flees")
class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Pray):
    pass
class Hawk(Predator):
    pass
class Fish(Pray, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()