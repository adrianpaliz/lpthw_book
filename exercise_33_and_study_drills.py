numbers_list = [] # Defined an empty list called numbers_list.
index = 0 # The index is defined to 0.

while index < 6: # The while loop repeatedly executes unlit the index be less than six. 
    print "At the top index is %d" % index # Frist indented line, string with formatting syntax for print each integer of index.
    numbers_list.append(index) # Use append method to add to numbers_list each integers from index.

    index = index + 1 # Increment index in one.
    print "Numbers now: ", numbers_list # Print plaint text and numbers_list until be less than six.
    print "At the bottom index is %d" % index # String for print the increment of index with formatiting syntax.


print "The numbers: " # Print plain text

for numbers in numbers_list: # For loop for iterating each integer of number_list.
     print numbers # Print each one of te integers in numbers_list.
