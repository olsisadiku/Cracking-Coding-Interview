
def rotate_matrix(matrix):
    size = len(matrix) - 1 
    start = 0
    for i in range(len(matrix)):
        for j in range(start, len(matrix[i])):
            temp = matrix[i][j]
            temp2 = matrix[j][abs(i-size)]
        
        if(start < len(matrix)):

            start+=1
        else:
            break
    return matrix




matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

rotate_matrix(matrix)