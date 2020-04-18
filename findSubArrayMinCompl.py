class MaxSubArraySum:
    def maxSubarraySum(inputArray, requiredSum):
        subArray = []
        low = 0
        high = 0
        sumCheck = 0
        sumCheck = inputArray[0]

        while (high >= low):

            if sumCheck == requiredSum:
                subArray.append(low)
                subArray.append(high)
                return subArray

            elif sumCheck > requiredSum :
                sumCheck = sumCheck - inputArray[low]
                low = low + 1

            else:
                sumCheck < requiredSum
                high = high + 1
                sumCheck = sumCheck + inputArray[high]


    values = [8,2,4,5,1,9]
    sum= 15
    print (maxSubarraySum(values,sum))

    def findSubArray(inputArray, desiredSum):
        result = []
        for i in range(0, len(inputArray) - 1):
            sumCheck = inputArray[i]
            for j in range(i + 1, len(inputArray) - 1):
                sumCheck = sumCheck + inputArray[j]
                if sumCheck == desiredSum:
                    result.append(i)
                    result.append(j)
                    return result
                if sumCheck > desiredSum:
                    break

    array = [8, 9, 5, 1, 2]
    sum = 15
    print(findSubArray(array, sum))
