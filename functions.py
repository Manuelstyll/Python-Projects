def myname():
    print("My name is Manuel")

myname()


# Parameters and Arguments
def fullname(firstname, lastname):
    print(firstname +" "+ lastname)

fullname("Manuel", "Holmes")

# Tuple as an Argument
def mygames(*games):
    print("My favorite game is" +games[0])

mygames("basketball", "tennis", "football")

# Key value arguments
def rank(position1, position2, position3):
    print("Student in position 1 is "+position1)

rank(position1="Manuel", position2="Baptiste", position3="Jason")