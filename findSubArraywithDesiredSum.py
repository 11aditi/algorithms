def findSumSubArray(A,desiredSum):
 low = 0
 high = 0
 sum = A[0]
 result = []
 while (high>=low):
  if sum == desiredSum :
   result.append(low)
   result.append(high)
   return result

  elif sum > desiredSum  :
   sum = sum - A[low]
   low = low +1

  else :
   high = high + 1
   sum = sum + A[high]


inputArray = [7,2,1,8,9]
findSum = 10
print (findSumSubArray(inputArray,findSum))

inputArray1 = [8,7,3,5,8,9,5,1,3]
findSum1 = 10
print (findSumSubArray(inputArray1,findSum1))
