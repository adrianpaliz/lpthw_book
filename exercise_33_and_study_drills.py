numbers_list = [] # A empty list
top_limit = range(0, 6) # top_limit now use range() function for create a sequence of numbers from 0 to 6

def for_loop(top_limit, increment): # Now the function is a for loop with two arguments.
    index = 0
    for limit in top_limit: # For loop for iterating each integer of the range.
        index < top_limit[limit]
        print("At the top index is {}".format(index))
        numbers_list.append(index)

        index += increment
        print("Number now:", numbers_list)
        print("At the bottom index is {}".format(index))


print("What should the increment be?")
increment = input("> ")
increment = int(increment)

for_loop(top_limit, increment) #Call the for_loop function.

print("The numbers: ")

for numbers in numbers_list:
     print(numbers)
