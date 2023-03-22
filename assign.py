q=1
w=2
e=3
r=4
t=5
y=6

def add (q,w):
    return(1+2)

def subtract (r,e):
    return(4-3)

def  multiply (q,w):
    return (1*2)

def divide (r,w):
    return (4/2)

print("Please select an operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice=input("Please enter choice 1/2/3/4:")

num_1 = int(input("Please enter first number:"))
num_2 = int(input("Please enter second number:"))

if choice == "1":
    print(num_1,"+",num_2,"=", add(1,2))


elif choice == "2":
    print(num_1,"-",num_2,"=", subtract(3,2))

elif choice == "3":
    print(num_1,"*",num_2,"=",multiply(4,6))

elif choice == "4":
    print(num_1,"/",num_2,"=", divide(4,2))

else:
    print("Invalid Input")
