def sum_row(row):
    result = 0
    for el in row:
        result += el
    return result

def sum_matrix(m):
    res=0
    for row in m:
        res+=sum_row(row)
    return res