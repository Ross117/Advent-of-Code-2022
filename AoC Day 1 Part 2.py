with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

input_cleaned = [int(value) if value != '' else value for value in input]

totals = []
calories = 0

for value in input_cleaned:
    if value == '':
        totals.append(calories)
        calories = 0
    else: 
        calories += value

totals.sort()

print(totals[len(totals) - 1] + totals[len(totals) - 2] + totals[len(totals) - 3])