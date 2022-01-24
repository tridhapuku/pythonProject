

def GetSetBitsOfNo(num):
    temp = num
    SetBit = 1
    countOfSetBit = 0
    NoOfIteration = 0

    while temp > 0:
        CheckSetBit = temp & SetBit
        temp = temp >> 1
        if CheckSetBit:
            countOfSetBit += 1
        NoOfIteration += 1

    # print(countOfSetBit)
    return countOfSetBit , NoOfIteration

def TotalCountOfSetBits( num):
    temp = num
    countOfSetBit = 0
    NoOfIteration = 0
    TotalNoOfIteration = 0
    sum = 0

    while temp > 0:
        sum,NoOfIteration  = GetSetBitsOfNo(temp)
        countOfSetBit = countOfSetBit + sum
        temp -= 1
        TotalNoOfIteration = TotalNoOfIteration + NoOfIteration
        # TotalNoOfIteration = TotalNoOfIteration +
    return countOfSetBit , TotalNoOfIteration

def TotalCountOfSetBitsOptimize(num):
    temp = num
    Rem = 0
    sum = 0
    count = 0
    NoOfRepeatedPattern1 = 0

    while temp > 0:

        if count == 0:
            sum = sum + (num >> 1)
            if num % 2 == 0:
                Rem = 0
            else:
                Rem = 1

            sum = sum + Rem

        else:
            DivideByPower2 = 1 << (count+1) #count=1 : DivideByPower2 = 4 , at2 , 8
            # print( ' no = {}'.format(1 << count))
            NoOfRepeatedPattern1 = (num >> (count+1)) << count  #count=1 : num/4 * 2 , count=2: num/8 * 4
            sum = sum + NoOfRepeatedPattern1

            Modulo = num % DivideByPower2

            if Modulo < (DivideByPower2 >> 1): #count= 1: Modulo = 0-1 , for 2-3: Rem = 1,2
                Rem = 0
            elif Modulo >= (DivideByPower2 >> 1) :
                Rem = Modulo - ((DivideByPower2 >> 1) - 1)

            sum = sum + Rem
        # print('Iteratn = {} NoOfRepeatedPattern= {} sum = {} Rem ={}'.format(count,NoOfRepeatedPattern1, sum, Rem))
        count += 1
        temp = temp >> 1

    return sum,count+1


#Test

num = 700000000000000000000000000000000000000000000000000000000000000000000
num2 = 1500000

print(TotalCountOfSetBitsOptimize(num))
print(TotalCountOfSetBits(num))


