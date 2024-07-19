# List Comprehensions are inline loops that produce a list

# syntax
# var = [<added item> for item in iterable]

# List comprehensio with a simple for loop
students = [1,2,3]

shirt_list = [num * 2 for num in students]
print(shirt_list)

other_list = []
for num in students:
    other_list.append(num * 2)

print(other_list)

print('=' *50)

# List comprehension with an if statment

# syntax
# var = [<added item> for item in iterable if (condition)]

nums = [1,2,3,4,5,6]

evens = [num for num in nums if num % 2 == 0]
print(evens)

even2 = []
for num in nums:
    if num % 2 == 0:
        even2.append(num)
print(evens)

print('=' *50)

# List comprehension with 'if' and 'else'

# syntax
# var = [<if True add> if (condition) else <else add> for item in iterable]

grades = [100, 98, 52, 87, 98, 68]

pass_fail = ['pass' if grade >= 70 else 'fail' for grade in grades]
print(pass_fail)