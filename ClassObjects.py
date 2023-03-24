class Computer:
    x = "mouse"

    def mycomputer(self):
         print("8gb", "500gb")

device=Computer()
v = type(device)
print(v)


y =device.x
print(y)

device.mycomputer()