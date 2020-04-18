
def findElementSortedRotatedArray(A,findElement):
 if findElement== None :
     return -1
 callRecursive= findPivotPosition(A)
 if (A[0]<= findElement <= A[callRecursive-1]) :
   return binarySearch(A,0,callRecursive-1,findElement)
 else:
   return binarySearch(A,callRecursive,len(A)-1,findElement)

def findPivotPosition(A) :
 start = 0
 end = len(A)
 while (start<=end) :
   mid = (start+end)//2
   if A[mid]> A[mid+1] :
      pivot = mid+1
      return pivot
   elif A[start]>=A[mid]:
      end = mid -1
   else :
     A[start]<= A[mid]
     start = mid+1

def binarySearch(A,start,end,findElement):
 while (start<=end) :
  mid = (start+end)//2
  if findElement == A[mid] :
     return mid
  elif findElement >= A[mid]:
     start = mid+1
  else :
     end = mid -1

inputArray = [82,84,86,88,76,78,80]
#inputArray = [76,78,64,68,70,72]
findElement = 78
#result = findElementSortedRotatedArray(inputArray,findElement)
result = findElementSortedRotatedArray(inputArray,findElement)
print ( "Element",findElement, "found at index:",result)