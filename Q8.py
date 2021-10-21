a = int(input('a = '))
b = int(input('b = '))

temp_a = a
temp_b = b

while temp_b != 0:
    temp = temp_a % temp_b
    temp_a = temp_b
    temp_b = temp

print("K.M.M =", a * b / temp_a)