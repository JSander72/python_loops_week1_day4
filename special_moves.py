
# Special moves

# break, continue, pass

#-- break : terminate a loop prematurely

pay_dirt = ['dirt', 'dirt', 'dirt', 'dirt', 'gold', 'dirt', 'dirt', 'dirt']

for scoop in pay_dirt:
    print("PANNING FOR GOLD")
    if scoop == 'gold':
        print("We found gold! Let's get outta here!!")
        break
    else:
        print("Just some more dirt, gotta keep lookin'")

print('='*50)

#-- continue : skip the rest of the current code block and moves onto the next interation in the loop

# square each number but only if it's odd
nums = [12, 256, 1146, 478, 21, 3457]

for num in nums:
    if num % 2 == 0:
        continue
    print("Original number: ", num)
    num **= 2
    print("Squared: ", num)

# pass : placeholder

my_list = [1,2,3]

for item in my_list:
    pass