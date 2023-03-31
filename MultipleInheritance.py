class Calculation1:
    def add(self,a,b):
        return a+b

class Calculation2:
    def subtract(self,a,b):
        return a-b

class Calculation3:
    def multiply(self,a,b):
        return a*b

class calculation(Calculation1,Calculation2,Calculation3):
    def divide(self,a,b):
        return a/b

c = calculation()
print(c.add(5,6))
print(c.subtract(6,4))