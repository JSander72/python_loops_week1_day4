
# nested for loops - allows us to loop through multiple lists or other iterable objects at once

# a loop insdie of a loop
# syntax of nested for loop
# for outer_var in outer_iterable:

nums = [1, 2, 3, 4, 5]
other = "this", "that", "another", "other"

for nun in nums:
    print("this is my outer loop: ", nun) # this loop will run 5 times, once for each number in nums
    for thing in other:
        print("this is my inner loop: ", thing) # this loop will run 4 times, once for each item in other, for each number in
        
print("*" * 50)

#-- Pizza topping combinations

pizza_type = ['deep dish', 'cicilian', 'NY stlye', 'Detroit']
toppings = ['pepperoni', 'sausage', 'ham', 'pineapple', 'olives']

for type1 in pizza_type:
    for topping in toppings:
        print("I have a ", type1, "pizza with", topping)

print('='*50)

for topping1 in toppings:
    for topping2 in toppings:
        if topping1 == topping2:
            print("Double", topping1)
        else:
            print(topping1, topping2)


