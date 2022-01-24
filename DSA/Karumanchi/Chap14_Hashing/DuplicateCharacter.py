
from collections import Counter

def find_dup_char(input):

    #Create dictionary
    WC = Counter(input)
    print(WC)
    j = -1

    for i in WC.values():
        j = j + 1
        if i > 1:
            print(WC.keys())

def printDuplicates(arr):
    dict = {}

    for elem in arr:
        try:
            dict[elem] += 1
        except:
            dict[elem] = 1


    for item in dict:
        if dict[item] > 1:
            print(item, end=' ')
#Test code

if __name__== "__main__":
    input = 'geeksforgeeks'
    # find_dup_char(input)
    printDuplicates(input)