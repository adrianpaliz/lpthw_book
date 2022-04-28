pair_numbers = [10, 8, 6 ,4, 2]

devices = ['laptop', 'smartwatch', 'screen', 'headphones']

priorities = [1, 'me', 2, 'partner', 3, 'family']


for number in pair_numbers:
    print("This is a pair number", number)

for device in devices:
    print("I already have a", device)

for priority in priorities:
    print("This is my priority", priority)

added_numbers = []
for number in range(6):
    print("Adding {} to the list".format(number))
    added_numbers.append(number)

for number in added_numbers:
    print("The number was:", number)
