def validate_position(target, neighbour, rows, cols):
    curr_pos = (target[0]+neighbour[0], target[1]+neighbour[1])
    if curr_pos[0] >= 0 and curr_pos[0] < rows and curr_pos[1] >= 0 and curr_pos[1] < cols:
        return curr_pos

neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]

def calc_defeat(m, target_pos):
    num_rows = len(m)
    num_cols = len(m[0])
    sum_of_matrix = 0

    for row in range(num_rows):
        for col in range(num_cols):
            sum_of_matrix += m[row][col]

    defeat = 0
    for neighbour in neighbours:
        if validate_position(target_pos, neighbour, num_rows, num_cols) != None:
            position = validate_position(target_pos, neighbour, num_rows, num_cols)
            if m[position[0]][position[1]] >= m[target_pos[0]][target_pos[1]]:
                defeat +=m[target_pos[0]][target_pos[1]]
            else:
                defeat += m[position[0]][position[1]]
    return sum_of_matrix - defeat

def matrix_bombing_plan(m):
    num_rows = len(m)
    num_cols = len(m[0])
    result = []
    for x in range (num_rows):
        for y in range (num_cols):
            result.append(calc_defeat(m, (x, y)))
    return result

#print (matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))