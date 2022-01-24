

def MaxProduct(Arr):
    LargestNo = float('-inf')
    SecondLargest = float('-inf')

    SmallestNegNo = float('inf')
    SecondSmallestNegNo = float('inf')

    for i in range(0,len(Arr)):

        if Arr[i] >= 0 and Arr[i] >= LargestNo:
            SecondLargest = LargestNo
            LargestNo = Arr[i]
        elif Arr[i] >=0 and Arr[i] < LargestNo and Arr[i] > SecondLargest:
            SecondLargest = Arr[i]

        elif Arr[i] < 0 and Arr[i] <= SmallestNegNo:
            SecondSmallestNegNo = SmallestNegNo
            SmallestNegNo = Arr[i]
        elif Arr[i] < 0 and SmallestNegNo < Arr[i] <= SecondSmallestNegNo:
            SecondSmallestNegNo = Arr[i]
        else:
            print('Arr[{}]= {}'.format(i, Arr[i]))

        print('Largest = {}, 2ndLargest={}'.format(LargestNo,SecondLargest))
        print('SmallestVe {}, 2ndSmallest={}'.format(SmallestNegNo, SecondSmallestNegNo))

    PositiveProduct = LargestNo * SecondLargest
    NegativeProduct = SmallestNegNo * SecondSmallestNegNo

    ResultArr = []
    print('PositveProd = {} , NegProd= {}'.format(PositiveProduct, NegativeProduct))
    if PositiveProduct != float('inf') and PositiveProduct >= NegativeProduct or NegativeProduct == float('inf') \
            or SmallestNegNo == float('inf') or SecondSmallestNegNo == float('inf') :
        ResultArr.append(LargestNo)
        ResultArr.append(SecondLargest)
    elif PositiveProduct < NegativeProduct or PositiveProduct == float('inf') \
            or SecondLargest == float('-inf') or LargestNo == float('-inf'):
        ResultArr.append(SmallestNegNo)
        ResultArr.append(SecondSmallestNegNo)

    return ResultArr


#TestCase

Arr = [1,4,3,6,7,0]

Arr2 = [-1, -3, -4, 2, 0, -5]
Arr3 = [ -4,-5,-1,-10,-6,0]
Arr4 = [0,0,1,0]
Arr5 = [1,2]
Arr6 = [-3,-4,-5,-1,0]
Arr7 = [0,0,-8,-1,0]


print(MaxProduct(Arr3))

