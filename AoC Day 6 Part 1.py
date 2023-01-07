with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read()

input_cleaned = []

for char in input:
    input_cleaned.append(char)

unique_chars = []
answer = ''

for index, char in enumerate(input_cleaned):

    if char not in unique_chars:
        unique_chars.append(char)
    else:
        ind = unique_chars.index(char)
        for i in range(ind, -1, -1):
            unique_chars.pop(i)
        unique_chars.append(char)

    if len(unique_chars) == 4:
        answer = index + 1
        break
        
print(answer)


