





def PrintSpiralMatrix(matrix , size):
    FirstRow = FirstColumn = 0
    MaxRow = MaxColumn = size - 1

    while MaxRow > FirstRow:

        for j in range(FirstColumn , MaxColumn + 1):
            print(matrix[FirstRow][j], end = ' ')

        print()

        for i in range(FirstRow , MaxRow+1):
            print(matrix[i][MaxColumn])

        for j in range(FirstColumn , MaxColumn + 1):
            print(matrix[MaxRow][j] , end=' ')

        print()

        for i in range(FirstRow , MaxRow + 1):
            print(matrix[i][FirstColumn])

        FirstRow += 1
        FirstColumn += 1
        MaxRow -= 1
        MaxColumn -= 1

def PrintMatrix(matrix):
    print('Printing Matrix ...')
    for i in range(row):
        print('[', end=' ')
        for j in range(col):
            # matrix[i][j] = k
            # k += 1
            print(matrix[i][j], end=' ')
        print(']')

def MatrixClockwiseRotation2(matrix, size):
    FirstRow = FirstColumn = 0
    MaxRow = MaxColumn = size - 1
    NewMatrix = [[0 for i in range(size)] for j in range(size)]

    while MaxRow > FirstRow:

        for j in range(FirstColumn,MaxColumn+1):
            if j != MaxColumn:
                NewMatrix[FirstRow][j+1] = matrix[FirstRow][j]
            # else:
            #     NewMatrix[FirstRow][j+1] = matrix[FirstRow][j]

        for i in range(FirstRow, MaxRow + 1):
            if i != MaxRow:
                NewMatrix[i+1][MaxColumn] = matrix[i][MaxColumn]
            # else:
            #     NewMatrix[i+1][MaxColumn] = matrix[i][MaxColumn]

        for j in range(FirstColumn, MaxColumn+1):
            if j != FirstColumn:
                NewMatrix[MaxRow][j-1] = matrix[MaxRow][j]
            # else:
            #     NewMatrix[MaxRow][j-1] = matrix[MaxRow][j]

        for i in range(FirstRow, MaxRow+1):
            if i != FirstRow:
                NewMatrix[i-1][FirstColumn] = matrix[i][FirstColumn]
            # else:
            #     NewMatrix[i-1][FirstColumn] = matrix[i][FirstColumn]

        FirstRow += 1
        FirstColumn += 1
        MaxRow -= 1
        MaxColumn -= 1
    return  NewMatrix


def MatrixClockwiseRotation(matrix, size):
    FirstRow = FirstColumn = 0
    MaxRow = MaxColumn = size - 1
    NewMatrix = [[0 for i in range(size)] for j in range(size)]

    while MaxRow > FirstRow:

        for j in range(FirstColumn,MaxColumn+1):
            if j == MaxColumn:
                NewMatrix[FirstRow+1][j] = matrix[FirstRow][j]
            else:
                NewMatrix[FirstRow][j+1] = matrix[FirstRow][j]

        for i in range(FirstRow, MaxRow + 1):
            if i == MaxRow:
                NewMatrix[i][MaxColumn-1] = matrix[i][MaxColumn]
            else:
                NewMatrix[i+1][MaxColumn] = matrix[i][MaxColumn]

        for j in range(FirstColumn, MaxColumn+1):
            if j == 0:
                NewMatrix[MaxRow-1][j] = matrix[MaxRow][j]
            else:
                NewMatrix[MaxRow][j-1] = matrix[MaxRow][j]

        for i in range(FirstRow, MaxRow+1):
            if i == 0:
                NewMatrix[i][FirstColumn+1] = matrix[i][FirstColumn]
            else:
                NewMatrix[i-1][FirstColumn] = matrix[i][FirstColumn]

        FirstRow += 1
        FirstColumn += 1
        MaxRow -= 1
        MaxColumn -= 1
    return  NewMatrix

def MatrixRotateACW90Deg(matrix,size):
    NewArr = [[0 for i in range(size)] for j in range(size)]

    FirstRow = FirstColumn = 0
    MaxRow = MaxColumn = size -1

    while MaxColumn > FirstColumn:
        i = MaxColumn
        for j in range(FirstColumn, MaxColumn + 1):
            # print('j ={} FirstColm={} MaxRow={}'.format(j,FirstColumn,MaxRow))
            NewArr[i][FirstColumn] = matrix[FirstRow][j]
            # PrintMatrix(NewArr)
            NewArr[i][MaxColumn] = matrix[MaxRow][j]
            NewArr[MaxRow][j] = matrix[j][FirstColumn]
            NewArr[FirstRow][j] = matrix[j][MaxColumn]
            i -= 1
        FirstRow += 1
        FirstColumn += 1
        MaxRow -= 1
        MaxColumn -= 1
    return NewArr





#Matrix Creation

row = col = 5

matrix = [[0 for i in range(col)] for j in range(row)]

#Adding Values to Matrix
k = 0
for i in range(row):
    print('[',end = ' ')
    for j in range(col):
        matrix[i][j] = k
        k += 1
        print(matrix[i][j],end=' ')
    print(']')

# PrintSpiralMatrix(matrix,row)
# RotatedMatrix = MatrixClockwiseRotation(matrix,row)
# PrintMatrix(RotatedMatrix)

# RotatedMatrix2 = MatrixClockwiseRotation2(matrix,row)
# PrintMatrix(RotatedMatrix2)

RotatedMatrix3 = MatrixRotateACW90Deg(matrix,row)
PrintMatrix(RotatedMatrix3)
# print(RotatedMatrix3)