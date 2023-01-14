with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

def is_visible(tree_height, start):

    row_ind, col_ind = start
    visible = True

    # search row left
    for i in range(col_ind - 1, -1, -1):
        if tree_height <= matrix[row_ind][i]:
            visible = False
            break
    
    if visible:
        return True

    visible = True

    # search row right
    for i in range(col_ind + 1, right_edge + 1, 1):
        if tree_height <= matrix[row_ind][i]:
            visible = False
            break
    
    if visible:
        return True

    visible = True

    # search col up
    for i in range(row_ind - 1, -1, -1):
        if tree_height <= matrix[i][col_ind]:
            visible = False
            break
    
    if visible:
        return True

    visible = True

    # search col down
    for i in range(row_ind + 1, bottom_edge + 1, 1):
        if tree_height <= matrix[i][col_ind]:
            visible = False
            break
    
    if visible:
        return True

    visible = True


matrix = [[int(elem) for elem in value] for value in input]

bottom_edge = len(matrix) - 1
right_edge = len(matrix[0]) - 1

count_of_visible = (len(matrix) * 2) + (len(matrix) * 2) - 4

trees_checked = 0

for row_ind, row in enumerate(matrix):
    
    if row_ind in [0, bottom_edge]:
        continue
    
    for col_ind, col in enumerate(row):
        
        if col_ind in [0, right_edge]:
            continue
        
        tree_height = col

        visible = is_visible(tree_height, [row_ind, col_ind])

        if visible:
            count_of_visible += 1

print(count_of_visible)