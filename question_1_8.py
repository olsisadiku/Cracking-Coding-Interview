def zero_matrix(matrix):
    row_contains = False
    
    for i in range(len(matrix)):
        zeros = []
        print(matrix[i])
        for j in range(len(matrix[i])):
            zeros += [0]
            if(matrix[i][j] == 0):
                row_contains = True
        if row_contains:
            matrix = matrix[:i] + [zeros] + matrix[i+1:]
            row_contains = False

    return matrix



matrix = [
    [1,1,1,1],
    [2,2,2,2],
    [3,3,0,3],
    [4,4,4,4]
]
print(zero_matrix(matrix))