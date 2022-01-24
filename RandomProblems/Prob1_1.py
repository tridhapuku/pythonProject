

def ReturnSum(listA ):
    listA.sort()
    sum = 0
    CountOfGivenElem = 0
    PrevNo = 0
    PresentNo = 0
    count = 0
    for i in listA:
        PrevNo = PresentNo
        PresentNo = i

        if PrevNo == PresentNo:
            CountOfGivenElem += 1
        elif PrevNo != PresentNo:
            if CountOfGivenElem % 2 != 0:
                sum = sum + (PrevNo * CountOfGivenElem)
                # print('sum = {}'.format(sum))
            CountOfGivenElem = 1


    #for last elem
    if CountOfGivenElem % 2 != 0:
        sum = sum + (PresentNo * CountOfGivenElem)

    return sum