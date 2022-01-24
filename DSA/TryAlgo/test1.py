# A O(n^2) Python3 program to
# count inversions of size 3

# Returns count of inversions
# of size 3
def getInvCount(arr, n):
    # Initialize result
    invcount = 0

    for i in range(1, n - 1):

        # Count all smaller elements
        # on right of arr[i]
        small = 0
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                small += 1

        # Count all greater elements
        # on left of arr[i]
        great = 0
        for j in range(i - 1, -1, -1):
            if (arr[i] < arr[j]):
                great += 1

        # Update inversion count by
        # adding all inversions that
        # have arr[i] as middle of
        # three elements
        invcount += great * small

    return invcount


# Driver program to test above function
arr = [8, 4, 2, 1]
arr = [5, 3,4, 2, 1]
n = len(arr)
print("Inversion Count :", getInvCount(arr, n))

# This code is Contributed by Smitha Dinesh Semwal
