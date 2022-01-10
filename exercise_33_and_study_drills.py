numbers_list = []

def while_loop(top_limit): # Convert the while loop in a function.
    index = 0 # Index now is indented as par of the function.
    while index < top_limit: # Now the top_limit is a variable
        print "At the top index is %d" % index
        numbers_list.append(index)

        index = index + 1
        print "Number now:", numbers_list
        print "At the bottom index is %d" % index

print "What should the top limit be?" # Print plain text.
top_limit = raw_input(">") # top_limit will be the integer that the user has entered in the prompt.
top_limit = int(top_limit) # Convert the input into a integer.

while_loop(top_limit) #Call the function.

print "The numbers: "

for numbers in numbers_list:
     print numbers
