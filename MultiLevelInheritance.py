class Employee:
    def eat(self):
        print("Eating")

class Manager(Employee):
    def task(self):
        print("Coordinating")

class Cook(Manager):
    def role(self):
        print("Cooking")

M = Manager()
M.task()

C = Cook()
C.role()

print(isinstance(M,Manager))
print(issubclass(Cook,Employee))
