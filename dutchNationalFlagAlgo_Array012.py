def dutchAlgo(inputArray) :
 low = 0
 mid = 0
 high = len(inputArray)-1
 while mid <=high :
   if inputArray[mid] == 0 :
     temp = inputArray[low]
     inputArray[low] = inputArray[mid]
     inputArray[mid] = temp
     low =low +1
     mid = mid +1
   elif inputArray[mid] == 1 :
     mid = mid +1
   else :
     inputArray[mid] == 2
     temp1 = inputArray[mid]
     inputArray[mid] = inputArray[high]
     inputArray[high] = temp1
     high = high -1
 return inputArray

values = [0, 1 ,2 ,0 , 2 ,1 ,0 ,0, 1, 2, 1, 2]
print (dutchAlgo(values))