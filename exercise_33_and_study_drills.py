numbers_list = []

def while_loop(top_limit, increment): # The function now has two arguments.
    index = 0
    while index < top_limit:
        print "At the top index is %d" % index
        numbers_list.append(index)

        index = index + increment # The variable increment will be added to index.
        print "Number now:", numbers_list
        print "At the bottom index is %d" % index

print "What should the top limit be?"
top_limit = raw_input(">")
top_limit = int(top_limit)

print "What should the increment be?" # Print plain text.
increment = raw_input(">") # increment will be the integer that the user has entered in the prompt.
increment = int(increment) # Convert the input into a integer

while_loop(top_limit, increment) # Call the while_ loop function

print "The numbers: "

for numbers in numbers_list:
     print numbers
