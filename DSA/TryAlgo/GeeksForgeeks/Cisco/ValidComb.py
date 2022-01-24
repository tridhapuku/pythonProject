

# Recursive implementation of numDecodings
def numDecodings(s: str) -> int:
    if len(s) == 0 or (len(s) == 1 and s[0] == '0'):
        return 0
    return numDecodingsHelper(s, len(s))

def numDecodingsHelper(s: str, n: int) -> int:
    if n == 0 or n == 1:
        return 1
    count = 0
    if s[n-1] > "0":
        count = numDecodingsHelper(s, n-1)
    if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7')):
        count += numDecodingsHelper(s, n - 2)
    return count


# Driver code
digits = "1234"
print("Count is ", numDecodings(digits))

