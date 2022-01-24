def Append0and1(listStr):
    count = 0
    TempList = listStr[:]
    LengthOfList = len(listStr)
    for i in range(0, 2 * LengthOfList):
        if count < LengthOfList:
            listStr[i] = '0' + TempList[i]
        else:
            listStr.append('1' + TempList[i - LengthOfList])
        count += 1
    return listStr


def GetlistStrBits(n):
    if n == 0:
        return []
    elif n == 1:
        return ['0', '1']
    else:
        return Append0and1(GetlistStrBits(n - 1))


listA = ['0', '1']
listB = ['00', '01', '10', '11']


# print(Append0and1(listB))

# print(GetlistStrBits(3))


class BacTrackingProblems:

    def __init__(self):
        self.NoOfInits = 0

    def CountOfInitCalls(self):
        self.NoOfInits += 1

    def Prob2_AppendSet1Set2(self, set1, set2):
        len1 = len(set1)
        len2 = len(set2)

        CombinedSet = []
        for i in range(len1):
            for j in range(len2):
                CombinedSet.append(set1[i] + set2[j])

        return CombinedSet

    def Prob2_GetAllString(self, set1, k):

        if k == 1:
            return set1
        elif k >= 2:
            return self.Prob2_AppendSet1Set2(self.Prob2_GetAllString(set1, k - 1), set1)


set1 = ['a', 'b', 'c']
set2 = ['a' , 'b']
k = 3

NewProb2 = BacTrackingProblems()
NewSet = NewProb2.Prob2_AppendSet1Set2(set1 , set2)

TestSetAllString = NewProb2.Prob2_GetAllString(set2,k)
print(NewSet)

print(TestSetAllString)
print('lenOf TestSetAllString = {}'.format(len(TestSetAllString)))
