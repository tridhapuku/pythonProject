

def Print(n):
    if n == 0:
        return 0
        # print(0)

    else:
        print(n)
        return Print(n-1)

def Factorial(n):

    if n== 0 | n == 1:
        return 1
    else:
        # return n*Factorial(n-1)
        return n+Factorial(n-1)

    return -1

def FibonacciNo(n):

    if n == 0 or n == 1:
        return n
    else:
        return FibonacciNo(n-1) + FibonacciNo(n-2)

if __name__ == '__main__':
    # print(Print(10))
    # print(Factorial(6))

    # print 10 fibonacci no
    # print(FibonacciNo(4))
    for i in range(0,9,1):
        print('i = {} Fibonacci = {}'.format(i , FibonacciNo(i)))