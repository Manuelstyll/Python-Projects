firstnumber = float(input("Enter first number:"))
Secondnumber = float(input("Enter second number:"))
operator = input("Enter operator:")

if operator == '+':
    print(firstnumber + Secondnumber)
elif operator == '-':
    print(firstnumber - Secondnumber)
elif operator == '*':
    print(firstnumber * Secondnumber)
elif operator == '/':
    print(firstnumber / Secondnumber)
else:
    print("Invalid Input")
