# Python3 program to sort an array of
# Roman Numerals in ascending order

# Function to return the value
# of a Roman symbol
def value(r):
    # I in roman is equal to
    # 1 in decimal
    if (r == 'I'):
        return 1

    # V in roman is equal to
    # 5 in decimal
    if (r == 'V'):
        return 5

    # X in roman is equal to
    # 10 in decimal
    if (r == 'X'):
        return 10

    # L in roman is equal to
    # 50 in decimal
    if (r == 'L'):
        return 50

    # C in roman is equal to
    # 100 in decimal
    if (r == 'C'):
        return 100

    # D in roman is equal to
    # 500 in decimal
    if (r == 'D'):
        return 500

    # M in roman is equal to
    # 1000 in decimal
    if (r == 'M'):
        return 1000

    return -1


# Function to return the decimal value
# of a roman numaral
def romanToDecimal(st):
    # Initialize result
    res = 0

    # Traverse given input
    i = 0
    while i < len(st):

        # Getting value of symbol s[i]
        s1 = value(st[i])

        if (i + 1 < len(st)):

            # Getting value of symbol s[i+1]
            s2 = value(st[i + 1])

            # Comparing both values
            if (s1 >= s2):

                # Value of current symbol
                # is >= the next symbol
                res = res + s1

            else:

                # Value of current symbol
                # is < the next symbol
                res = res + s2 - s1
                i += 1

        else:
            res = res + s1

        i += 1

    return res


# Function to sort the array according to
# the increasing order
def sortArr(arr, n):
    # Vector to store the roman to integer
    # with respective elements
    vp = {}

    # Inserting roman to integer
    # with respective elements in vector pair
    for i in range(n):
        p = romanToDecimal(arr[i])
        vp[p] = arr[i]

    # Sort the vector, this will sort the pair
    # according to the increasing order.
    for i in sorted(vp):
        print(vp[i], i)


# Driver code
if __name__ == "__main__":
    arr = ["MCMIV", "MIV",
           "MCM", "MMIV"]
    n = len(arr)

    sortArr(arr, n)

# This code is contributed by chitranayal
