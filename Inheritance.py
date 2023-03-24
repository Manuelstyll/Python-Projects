class Animal:
    alive = True

    def eat(self):
      print("It is eating")

    def sleep(self):
      print("It is sleeping")

class Fish(Animal):
    pass

fish = Fish()
fish.eat()

# Inheritance 2
class Child:
    alive = True

    def cry(self):
        print("It is crying")

class Son(Child):
    pass

James = Child()
James.cry()


