import string

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

items = []

for i in range(0, 300, 3):
    for item in input[i]:
        if item in input[i + 1] and item in input[i + 2]:
            items.append(item)
            break

scores = {}

for index, letter in enumerate(string.ascii_lowercase):
    scores[letter] = index + 1

for index, letter in enumerate(string.ascii_uppercase):
    scores[letter] = index + 27

sum_priorities = 0

for item in items:
    sum_priorities += scores[item]

print(sum_priorities)

