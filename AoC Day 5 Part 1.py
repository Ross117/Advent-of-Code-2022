import re

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

def filter_start(str):
    return str.find('move')

def filter_rest(str):
    return str.find('move') + 1

start = list(filter(filter_start, input))[:8]

start.reverse()

stacks = [[] for i in range(9)]

j = 0
for i in range(1, 35, 4):
    for value in start:
        if not value[i] == ' ':
            stacks[j].append(value[i])
    j += 1

instructions = list(filter(filter_rest, input))

def return_numbers(str):

    return re.findall('\d+', str)

instructions = [return_numbers(value) for value in instructions]

for instruction in instructions:
    quant, start, end = instruction

    quant = int(quant)
    start = int(start) - 1
    end = int(end) - 1
    
    for i in range(quant):
        stacks[end].append(stacks[start][-1])
        stacks[start].pop(-1)

top_crates = [stack[-1] for stack in stacks]

print(''.join(top_crates))