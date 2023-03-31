# Parameterised Constructors
class Employee:
    def __init__(self,firstname,lastname,id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def info(self):
      print(self.firstname,self.lastname,self.id)

e = Employee("Manuel","eMobilis",3)
e.info()

print(getattr(e,"firstname"))
print(getattr(e,"lastname"))
print(hasattr(e,"age"))

# Non Parameterised Constructor
class Student:
    def __init__(self):
        print("No Parameter available")

    def display(self,name,course,age):
        self.name = name
        self.course = course
        self.age = age
        print(self.name,self.course,self.age)

stu = Student()
stu.display("One","MIT",36)
print(getattr(stu,"course"))



