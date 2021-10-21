import random

n = int(input("Please enter size of array: "))
numbers = []

for i in range(n):
    random_number = random.randint(0, 100)
    if random_number in numbers:
        while random_number in numbers:
            random_number = random.randint(0, 100)
        numbers.append(random_number)
    
    else:
        numbers.append(random_number)

print("Array =", numbers)