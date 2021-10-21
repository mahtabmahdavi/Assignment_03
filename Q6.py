numbers = []

length = int(input("How many numbers do you want to enter? "))

for i in range(length):
    number = int(input("Please enter a number: "))
    numbers.append(number)


for i in range(len(numbers)-1):
    if numbers[i+1] >= numbers[i]:
        if i+1 == len(numbers)-1:
            print("It's SORTED!")
        else:
            continue
    else:
        print("It's NOT SORTED.")
        break


