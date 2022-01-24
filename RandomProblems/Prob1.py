



def ReturnSum(listA ):

    print(listA)
    listA.sort()
    # listB = listA
    # print(listB)
    sum = 0
    CountOfGivenElem = 0
    PrevNo = 0
    PresentNo = 0
    count = 0
    for i in listA:
        # print('elem = {}'.format(i))
        PrevNo = PresentNo
        PresentNo = i

        if PrevNo == PresentNo:
            CountOfGivenElem += 1
        elif PrevNo != PresentNo:
            # print(CountOfGivenElem)
            if CountOfGivenElem % 2 != 0:
                sum = sum + (PrevNo * CountOfGivenElem)
                # print('sum = {}'.format(sum))
            CountOfGivenElem = 1


    #for last elem
    if CountOfGivenElem % 2 != 0:
        # print('sum = {}'.format(sum))
        sum = sum + (PresentNo * CountOfGivenElem)

    return sum


listA = [11,11,12,12,13,13,13]
listB = [100,200,300,40,40]

print(ReturnSum(listA))


