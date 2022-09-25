


def CheckIfTru(arr , n):

    len1 = len(arr)
    count = 0
    if len1 == 0:
        count = 0

    if len1 == 1 and arr[0] == 0:
        count = 1

    if len1 == 1 and arr[0] == 1:
        count = 0

    if len1 == 2 :
        if arr[0] == 0 and arr[1]== 0:
            count = 1
        elif arr[0] == 1 or arr[1] == 1:
            count = 0

    if n <= count :
        return True

    if len1 > 2:

        # for i in range(1,len1-1, 2):
        i = 1
        while i <= len1 - 3:
            if arr[i] == 0 and arr[i-1] == 0 and arr[i+1] == 0:
                count = count + 1
                i = i + 2
            elif arr[i] == 1:
                i = i + 2
            else:
                i = i + 1

        #check for last 2 elems
        if arr[len1-2] == 0 and arr[len1-1] == 0:
            count = count + 1

    if n <= count:
        return True

    return False


# arr = [0,1,0,0,0]
arr = [1,0,0,0,0,1]

n = 1

print(CheckIfTru(arr , n))

