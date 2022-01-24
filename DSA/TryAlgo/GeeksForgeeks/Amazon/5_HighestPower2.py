

def HighestPower2(num):
    temp = int(num)
    count = 0
    GreatestNo = 1

    while temp != 1:
        temp = temp >> 1
        GreatestNo = GreatestNo << 1
        count +=1
    return GreatestNo ,count

def HighestPower2Optimise(num):
    temp = num
    div = 250
    ToDiv = div
    result = 0
    DesiredNo = 1
    count = 0
    if num <= 0:
        return -1

    while result != 1:
        result = num >> ToDiv
        count += 1
        if result > 1:
            div = div >> 1
            ToDiv = ToDiv + div
        elif result == 0:
            div = div >> 1
            ToDiv = ToDiv - div
        elif result == 1:
            DesiredNo = 1 << ToDiv

    return DesiredNo,count


#Test case

num = 700000000000000000000000000000000000000000000000000000000000000000000

print(HighestPower2(num))
print(HighestPower2Optimise(num))