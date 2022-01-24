
#Here, we will have 2-D Array declaration & use

rows , cols = (50,50)
arr = [[0 for i in range(cols)] for j in range(rows)]

print(arr)

# exit()
arr[0][0] = 5
arr[0][1] = 10

print(arr)
no = 1
rows , cols = (5,5)
for i in range(rows):
    for j in range(cols):
        arr[i][j] = no * 2
        no = no << 1

for i in range(rows):
    print('[', end='')
    for j in range(cols):
        # if j == cols - 1:
        print(arr[i][j], end=' ')
        # else:
        #     print(arr[i][j], end=' ')
    print(']')