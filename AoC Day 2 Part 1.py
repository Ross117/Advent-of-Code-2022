with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3 
}

outcomes = {
    'win': ['C X', 'B Z', 'A Y'],
    'loss': ['A Z', 'C Y', 'B X']
}

total_score = 0

for game in input:

    selection = game[2]

    score = scores[selection]

    if game in outcomes['win']:
        score += 6
    elif game not in outcomes['loss']:
        score += 3

    total_score += score

print(total_score)