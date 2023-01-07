with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3 
}

outcomes = {
    'A': {
        'win': 'Y',
        'loss': 'Z',
        'draw': 'X'
    },
    'B': {
        'win': 'Z',
        'loss': 'X',
        'draw': 'Y'
    },
    'C': {
        'win': 'X',
        'loss': 'Y',
        'draw': 'Z'
    },
}

total_score = 0

for game in input:

    indicator = game[2]
    opponent = game[0]

    if indicator == 'X':
        selection = outcomes[opponent]['loss']
        score = 0
    elif indicator == 'Y':
        selection = outcomes[opponent]['draw']
        score = 3
    elif indicator == 'Z':
        selection = outcomes[opponent]['win']
        score = 6

    score += scores[selection]

    total_score += score

print(total_score)