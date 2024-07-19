# Intro to For Loops

# for loops allow us to execute a code block for every item in an iterable (string, list, ... )

# they allow us to repeat code a limiteed number of times (number of times is determined by the iterable)

#Syntex of for loop

# for it in iterable:
    # code block

flavors = ['chocolate', 'vanilla', 'strawberry', "cookies n cream", "orange sherbet", "caramel"]

for flavor in flavors:
    # print(flavor) # print each flavor in the list
    print("Tasting the", flavor, "flavor!") # print a statement for each flavor

    # you can add code here to perform actions based on the flavor
print("*"*50)

# as we loop over an iterable we gret to isolate each iten and chan choose to do soemthing with that item or not 

guest_list = ["Dylan", "Emma", "Noah", "Olivia", "Sophia", "Adam"]

line = ["Adam", "Ben", "Emma", "David", "Noah", "Frank"]

# door man for loop

for person in line: # person is a variable that will take on each value in the line list - it can be anything instead of person (fool, clown, pie, chair,...)
    print("*", person, "walks up to the bouncer *")
    if person in guest_list:
        print(person, "is welcome to the party!")
    else:
        print("Get outta here!!! you're not on the guest list tonight!")
    print("=" * 50) # add a line break after each person loop - since it runs the same code over and over it will put the line at the end each time it runs through the code block

print("*" * 50)

submitted_homework = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
attended_class = ["Alice", "Bob", "Charlie", "David", "Eve"]

for student in submitted_homework:
    if student in attended_class:
        print(student, "has submitted homework and has attended class!")
    else:
        print(student, "has submitted homework but has not attended class.")
    print("=" * 50)
print("*" * 50)

nums = [1, 2, 3, 4, 5, 6, 7]
for num in nums:
    if num % 2 == 0: # means 2 went into num exactly amount of times (no remainder)
        print(num, "is even")
    else:
        print(num, "is odd")

print("*" * 50)

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

above_100 = []
for temp in temperatures:
    if temp > 100: # loops through each temperature and if it's greater than 100, it adds it to the above
        above_100.append(temp) # adds the temperature to the list

print(above_100) # prints the list of temperatures above 100




