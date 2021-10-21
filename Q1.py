import random

words_bank = ['tree', 'book', 'linux', 'python', 'java', 'sadjad', 'rock', 'javascript', 'up', 'blue', 'pepperoni', 'song', 'car', 'book', 'pen']

word = random.choice(words_bank)
life = 7
user_true_chars = []

while True:

    flag = 1
    
    for i in range(len(word)):
        if word[i] in user_true_chars:
            print(word[i], end = '')
        else:
            flag = -1
            print('-', end = '')
            
    if flag == 1:
        print("\nYou win 🎉")
        break

    if life == 0:
        print("\nGame Over!")
        print("\"", word, "\"")
        break

    user_char = input("\nPlease enter a character: ")

    if user_char in word:
        user_true_chars.append(user_char)
        print('✅')
    else:
        life -= 1
        print('❌')