
def rotate_matrix(matrix):
    size = len(matrix) - 1 
    length = len(matrix)
    start = 0
    for i in range(len(matrix)):
        for j in range(start, length-start):
            top = matrix[i][j]
            print("I:", i, "J:", j)

            right = matrix[j][abs(i-size-start) % length]
            print("I:", j, "J:", abs(i-size-start) % length)
            
            bottom = matrix[abs(i-size-start) % length][abs(j-size-start) % length]
            print("I:", (abs(i-size-start) % length), "J:", abs(j-size-start) % length)

            left = matrix[abs(j-size-start) % length ][abs(i-size-start+size) % length]
            print("I:", abs(j-size-start) % length, "J:", abs(i-size-start+size) % length )

            matrix[j][abs(i-size-start) % length] = top

            matrix[abs(i-size-start) % length][abs(j-size-start) % length] = right

            matrix[abs(j-size-start) % length ][abs(i-size-start+size) % length] = bottom

            matrix[i][j] = left 

            print()
            print()

        if(start < length):
            start+=1
        else:
            break
    return matrix




matrix = [
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3],
    [4,4,4,4]
]

print(rotate_matrix(matrix))