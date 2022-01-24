

def PrintChess(num):
    arr2D = [['B' for i in range(num)] for j in range(num)]

    for i in range(num):
        for j in range(num):
            if ((i+j) % 2) == 0:
                arr2D[i][j] = 'W'

    return arr2D

num = 400

print(PrintChess(num))