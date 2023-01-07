with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

input_cleaned = [value.split(',') for value in input]

rngs = []

for pair in input_cleaned:
    pair_rngs = []
    for value in pair:
        lst = value.split('-')
        lst_cleaned = [int(value) for value in lst]
        rng = []
        for i in range(lst_cleaned[0], lst_cleaned[1] + 1):
            rng.append(i)
        pair_rngs.append(rng)
    rngs.append(pair_rngs)

overlap = 0

for pair in rngs:
    if set(pair[0]).issubset(pair[1]) or set(pair[1]).issubset(pair[0]):
        overlap += 1

print(overlap)

