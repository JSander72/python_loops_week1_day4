
# range() creates a sequece of numbers that we can iterate through

print(list(range(11)))

for num in range(11):
    print(num)

# range (start, stop, step) : creates a sequence of numbers starting from start and ending before stop, with a step of step (non-inclusive) 

print("Range of numbers from 5 - 10")
list_of_nums = []

for num in range(5,11): # creates a list of numbers from 5 to 10 (non-inclusive)
    list_of_nums.append(num)

print(list_of_nums)

list_of_nums = list(range(5,11)) # creat a list of nums by type casting my range sequence to a list
print(list_of_nums)

# range (start, stop, step)

print("Printing a range of numbers from 10 to 100, every 10th digit")
for num in range(10, 101, 10): # creates a list of numbers from 5 to 10 (non-inclusive)
    print(num)

print("Printing only the even numbers in this range")
for num in range(0, 21, 2):
    print(num)

print("Printing only even numbers from 20 to 0")
for num in range(20, 0, -2):
    print(num)

print("*" * 50)

# range() in combination with len()

alist = ["item1", "item2", "item3", "item4", "item5"]
print(len(alist)) # prints the length of the list

for index in range(len(alist)):
    print(index, alist[index]) # allows to access the loop with the index ( so if the loop normally does cover the iterable, we can access each item by its index )

print("*" * 50)

food = ("tacos", "burgers", "fries", "pizza", "sushi", "steak", "tiramisu", "mozzarella sticks", "omelette", "risotto")
for index in range(len(food)):
    if food [index] == "burgers":
        print("burgers position: ", index)

print("*" * 50)

students = ("John", "Jim", "Jane", "Jill", "Jack")
grades = (85, 90, 78, 95, 100)
activites = ("football", "chess", "reading", "swimming", "basketball")

for index in range(len(students)):
    print(students[index], "has a grade of", grades[index], "and participated in", activites[index]) # this access the index of each varable mentioned ( each list has the same number of index so they all correspond)  I can loop through all 3 list creeated : students, grades, activies at the same time
print("*" * 50)

grouped_info = zip(students, grades, activites) # zip combines multiple lists into a single list of

for item in zip(students, grades, activites): #zip function combines elements from each list into a tuple
    print(item) # prints each tuple (student, grade, activity) together
    print("Student:", item[0], "Grade:", item[1], "Activity:", item[2]) # prints each item separately

print("*" * 50)



