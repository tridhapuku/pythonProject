import numpy as np

num = 1000
r1 = c1 = r2 = c2 = num
# r1 , c1 = (3,3)
# r2 , c2 = (3,3)
arr1 = [[0 for i in range(c1)] for j in range(r1)]

arr2 = [[0 for i in range(c2)] for j in range(r2)]

resArr = [[0 for i in range(c2)] for j in range(r1)]

#Arr1 & Arr2
k = 0
for i in range(r1):
    for j in range(c1):
        k += 1
        arr1[i][j] = arr2[i][j] = k


# print(arr1[0])
# arr1[0]  = 199
# print(arr1[1])
# print(len(arr1[1]))
# print(arr1)
# print(arr2)

resArrNp = np.dot(arr1,arr2)
print(resArrNp)
#Product
for i in range(r1):
    for j in range(c2):
        sum = 0
        for k in range(c1):
            sum = sum + arr1[i][k] * arr2[k][j]

        resArr[i][j] = sum

# print(resArr)