# physics calcy

operations = [ "Preassure" , "Force" , "Speed" , "Velocity" , "Accelaration" , "Momentum" ]

#pre code sector I
# preassure function to calculate preassure
def preassure():
    print(" ")
    force = int(input("Enter force : "))
    print(" ")
    area = int(input("Enter area : "))
    preassure = force / area
    print(" ")
    print("Preassure is " + str(preassure) + "pascal")

# force function to calculate force
def force():
    print(" ")
    mass = int(input("Enter mass : "))
    print(" ")
    accelaration = int(input("Enter accelaration : "))
    force = mass * accelaration
    print(" ")
    print("Force is " + str(force) + "newton")

# speed func to calculate speed of object
def speed():
    print(" ")
    distance = int(input("Enter distance : "))
    print(" ")
    time = int(input("Enter time taken : "))
    speed = distance / time
    print(" ")
    print("Speed of object is " + str(speed))

# velocity func to calculate velocity of object
def velocity():
    print(" ")
    displacement = int(input("Enter displacement : "))
    print(" ")
    time = int(input("Enter time taken : "))
    velocity = displacement / time
    print(" ")
    print("Velocity of object is " + str(velocity))

# accelaration func to calculate accelaration
def accelaration():
    print(" ")
    initialV = int(input("Enter initial velocity : "))
    print(" ")
    finalV = int(input("Enter final velocity : "))
    print(" ")
    time = int(input("Enter time taken : "))
    acce = (finalV - initialV) / time
    print(" ")
    print("Accelaration is " + str(acce) + "m/s sq.")

# monentum func to calculate momentum
def moment():
    print(" ")
    mass = int(input("Enter mass : "))
    print(" ")
    velocity = int(input("Enter velocity : "))
    print(" ")
    momentum = mass * velocity
    print(" ")
    print("Momentum is " + str(momentum))

# CLI code sector II

while True:
    print(" ")
    print("Hello")
    print(" ")
    startOrEnd = input("Start or End : ")
    print(" ")
    if startOrEnd.strip() == "Start" :
        for op in operations:
            print(op)
            print(" ")

        main = input("Which operation : ")
        if main.strip() == "Preassure":
            print(preassure())
            continue
        elif main.strip() == "Force":
            print(force())
            continue
        elif main.strip() == "Speed":
            print(speed())
            continue
        elif main.strip() == "Velocity":
            print(velocity())
            continue
        elif main.strip() == "Accelaration":
            print(accelaration())
            continue
        elif main.strip() == "Momentum":
            print(moment())
            continue
        else :
            print("Invalid operation")
            continue
    elif startOrEnd.strip() == "End":
        print("...Progarm Ended...")
        break