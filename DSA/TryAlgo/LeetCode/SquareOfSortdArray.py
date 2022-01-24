

def SquareOfSortedArr(list1 ):
    lenlist = len(list1)
    count = i = 0
    IndxAtLast = j = lenlist - 1
    ResultList = [ 0 ] * lenlist

    while count < lenlist:

        if list1[i] < 0 and list1[j] > 0:
            sq1 = list1[i] * list1[i]
            sq2 = list1[j] * list1[j]

            if sq1 > sq2 :
                i = i + 1
                ResultList[IndxAtLast] = sq1
            else:
                j = j - 1
                ResultList[IndxAtLast] = sq2
        elif list1[i] >= 0 and list1[j] > 0:
            sq2 = list1[j] * list1[j]
            ResultList[IndxAtLast] = sq2
            j -= 1
        elif list1[i] <= 0 and list1[j] <= 0:
            sq1 = list1[i] * list1[i]
            ResultList[IndxAtLast] = sq1
            i += 1
        else:
            print('SOme case missing , count = {}'.format(count))
            print('i = {} , j ={}'.format(i,j))
        count += 1
        IndxAtLast -= 1

    return ResultList

Input1 = [-3,-2,-1,0,2,5,6]
Input2 = [-3,-2,-1]
Input3 = [2,5,6]
Input4 = [-4]
Input5 = []
print(SquareOfSortedArr(Input1))


