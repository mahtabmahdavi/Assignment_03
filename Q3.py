from typing import Counter


sentence = input("Enter a sentence: ")

word_counter = 0

for i in range(len(sentence)):
    if sentence[i] == ' ':
        word_counter += 1

print("Number of words in this sentence =", word_counter + 1)