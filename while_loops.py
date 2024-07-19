# While loops allow us to run a code block while a certain condition remains True

# it will continue to run until the specified condition is False or until we break out of the loop

# syntax
# while (condition):
#     run code block

bus = []

# my bus can only hold 5 people in it

while len(bus) < 5:
    print("Letting a person on the bus...")
    bus.append('person')
    print("There are", len(bus), "people on the bus right now")

print(bus)

# be careful about infinite loops!

flag = True

while flag:
    user = input("Say something, but if you wanna quit, then say so!")
    if user == 'quit':
        # flag = False
        break


# watch out for failure to launch

# the loop's condition starts as False and never runs

bus = []

while len(bus) > 5:
    print("Letting a person on the bus...")
    bus.append('person')
    print("There are", len(bus), "people on the bus right now")