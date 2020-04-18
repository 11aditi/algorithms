def array(list):
    # result=[]
    list.reverse()
    print(list)


def revArray(inputArray):
    low = 0
    high = len(inputArray) - 1
    mid = (low + high) / 2
    while low < mid < high:
        temp = inputArray[low]
        inputArray[low] = inputArray[high]
        inputArray[high] = temp
        low = low + 1
        high = high - 1
    return inputArray



value = [2, 3, 4, 6, 7, 7, 8]
value1 = [5, 4, 7, 8, 9, 0, 23, 6, 7]
print(revArray(value))
print(revArray(value1))
