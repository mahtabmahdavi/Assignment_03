number = int(input('Please enter a number: '))

number_of_digits = len(str(number))
sum = 0
temp_number = number

while temp_number > 0:
    digit = temp_number % 10
    sum += digit ** number_of_digits
    temp_number //= 10

if number == sum:
    print("yes")
else:
    print("no")
