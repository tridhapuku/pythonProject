import numpy as np


def CheckDiagonalSum(bo, n):
    for i in range(0, n):
        j = sum1 = sum2 = sum3 = sum4 = 0
        for k in range(0, n - i):
            sum1 = sum1 + bo[i + k][j + k]
            sum2 = sum2 + bo[j + k][i + k]
            sum3 = sum3 + bo[n - 1 - i - k][j + k]
            sum4 = sum4 + bo[n - 1 - k][i + k]

        if sum1 > 1 or sum2 > 1 or sum3 > 1 or sum4 > 1:
            return False
    return True


arr = np.zeros((4, 4), dtype=int)

# print(arr)

# arr[2,3] = 1
arr[1, 0] = 1
arr[0, 1] = 1
# arr[2,1] = 1

# print(arr)
#
# print(CheckDiagonalSum(arr, 4))


def validate(bo, n):
    for row in range(0, n):
        if sum(bo[row,]) > 1:
            return False

    for col in range(0, n):
        if sum(bo[:, col]) > 1:
            return False

    diags = [bo[::-1, :].diagonal(i) for i in range(-n + 1, n)]
    # print(bo[::-1,:])
    # print(len(diags))
    # print(type(diags))
    # print(diags)

    diags.extend(bo.diagonal(i) for i in range(n - 1, -n, -1))
    # print(len(diags))
    # print(diags)
    for x in diags:
        if len(x) > 1:
            if sum(x) > 1:
                return False

    return True


print(validate(arr, 4))

def solve(bo, col, n):
    if validate(bo,n):
        if bo.sum() == n:
            return True

        for row in range(0,n):
            bo[row,col] = 1
            if validate(bo,n):
                if solve(bo,col+1,n):
                    return True
                bo[row,col] = 0
            else:
                bo[row,col] = 0

    return False


MatrixSize = 15
board = np.zeros((MatrixSize , MatrixSize), dtype= int)

if MatrixSize > 15:
    print('It will be very slow for MatrixSize > {}'.format(MatrixSize))
    input1 = input('ENter y to coninue')
    if input1 == 'y' or input1 == 'Y':
        if solve(board,0,MatrixSize):
            print(board)
        else:
            print('Not possible')
    else:
        print('You don\'t want to solve')
else:
    if solve(board, 0, MatrixSize):
        print(board)
    else:
        print('Not possible')