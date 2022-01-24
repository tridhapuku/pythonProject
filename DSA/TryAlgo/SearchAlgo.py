


def BinarySearch(listA , num):
    lengthOfListA = len(listA)

    l = 0
    r = lengthOfListA
    while(l <=r ):
        middle = int((l+r)/2)

        if num == listA[middle]:
            return middle
        elif num > listA[middle]:
            l = middle + 1
        else:
            r = middle - 1

    #still num is not found
    return -1


listA = [5, 15 , 25 , 40 , 55]

print(BinarySearch(listA,40))

print(BinarySearch(listA, 45))
