import string

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

input_cleaned = [[value[0:(len(value)//2)], value[(len(value)//2):]] for value in input]

items = []

for rucksack in input_cleaned:
    common_item = ''
    for item in rucksack[0]:
        if item in rucksack[1]:
            common_item = item
            items.append(common_item)
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