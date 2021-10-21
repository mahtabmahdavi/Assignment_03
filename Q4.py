number = int(input('Please enter a number: '))

temp_number = number
fact = 1
counter = 1

while fact < number:
    counter += 1
    fact *= counter

if number == fact:
    print("yes")
else:
    print("no")
