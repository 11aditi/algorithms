def bubbleSort(inputArray):
    # sortedArray = 0
    for element in range(0, len(inputArray) - 1):
         for num in range(0,len(inputArray)-1 ):
            if inputArray[num] > inputArray[num + 1]:
                temp = inputArray[num]
                inputArray[num] = inputArray[num + 1]
                inputArray[num + 1] = temp
                # sortedArray = 1
                # return True
        # if sortedArray == 0 :
        # break
    return inputArray

values = [9, 7, 5, 6, 4, 2, 3]
Result = bubbleSort(values)
print("sorted Array is:", Result)
