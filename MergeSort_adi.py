#class mergeSort:
def breakArray(inputArray, low, high):
        if high-low >1:
            mid = (low + high) // 2
            breakArray(inputArray, low, mid)
            breakArray(inputArray, mid, high)
            mergeSort(inputArray,low,mid,high)

def mergeSort(inputArray,low,mid,high):
        leftArray = inputArray[low:mid]
        rightArray = inputArray[mid: high]
        print ("Left length",len(leftArray))
        print ("Right length", len(rightArray))
        i = 0
        j = 0
        k = low
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                inputArray[k] = leftArray[i]
                i = i + 1
            else:
                inputArray[k] = rightArray[j]
                j = j + 1
            k = k + 1


        while i <  len(leftArray) :
            inputArray[k] = leftArray[i]
            i=i+1
            k = k + 1

        while j <  len(rightArray):
            inputArray[k] = rightArray[j]
            j=j+1
            k = k + 1

values = [9,7,1,2,3,8]
breakArray(values, 0, len(values))
print (values)