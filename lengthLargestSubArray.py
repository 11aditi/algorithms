def largestIncreasingSubarray(inputArray):
    low = 0
    high = 1
    n= len(inputArray)
    currentCount = 1
    maxCount=0
    while (high<n):
        if inputArray[low] < inputArray[high]:
            low = low+1
            currentCount = currentCount+1
            high = high+1
            maxCount=max(currentCount,maxCount)
        else :
            low = low+1
            high = high+1
            currentCount= 1
    print ("The length of largest sub-array is:", maxCount)

A = [78,88,98,108,109,111,4,22,44]
largestIncreasingSubarray(A)

B = [8,7,3,5,8,9,1,1,3]
largestIncreasingSubarray(B)

largestIncreasingSubarray([1,2,38,7,31,2,3,4,5,6,7,8,9,5,8,9,1,1,3])





