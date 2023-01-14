with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

def get_viewing_distances(tree_height, start):

    row_ind, col_ind = start

    viewing_distances = []

    # search row left
    score_1 = 0
    for i in range(col_ind - 1, -1, -1):
        score_1 += 1
        if tree_height <= matrix[row_ind][i]:
            break

    viewing_distances.append(score_1)

    # search row right
    score_2 = 0
    for i in range(col_ind + 1, right_edge + 1, 1):
        score_2 += 1
        if tree_height <= matrix[row_ind][i]:
            break

    viewing_distances.append(score_2)

    # search col up
    score_3 = 0
    for i in range(row_ind - 1, -1, -1):
        score_3 += 1
        if tree_height <= matrix[i][col_ind]:
            break

    viewing_distances.append(score_3)

    # search col down
    score_4 = 0
    for i in range(row_ind + 1, bottom_edge + 1, 1):
        score_4 += 1
        if tree_height <= matrix[i][col_ind]:
            break

    viewing_distances.append(score_4)

    return viewing_distances[0] * viewing_distances[1] * viewing_distances[2] * viewing_distances[3]


matrix = [[int(elem) for elem in value] for value in input]

bottom_edge = len(matrix) - 1
right_edge = len(matrix[0]) - 1

count_of_visible = (len(matrix) * 2) + (len(matrix) * 2) - 4

trees_checked = 0

scores = []

for row_ind, row in enumerate(matrix):
    
    for col_ind, col in enumerate(row):
        
        tree_height = col

        viewing_distances = get_viewing_distances(tree_height, [row_ind, col_ind])
        scores.append(viewing_distances)

scores.sort(reverse=True)

print(scores[0])