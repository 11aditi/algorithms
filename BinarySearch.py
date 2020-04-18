#class definition starts, a class can have many functions and varaibles.
# All the functions and variables presnt inside cllass are its memebers
class BinarySearchClass:
    #function definition starts
    def FindArrayElement (sortedInputArray, elementToBeSearched) :
        low = 0
        high = len(sortedInputArray)-1
        while ( low<=high) :
            mid =int( (low+high)/2)
            if sortedInputArray[mid] == elementToBeSearched :
                return mid
            elif sortedInputArray[mid] > elementToBeSearched :
                high = mid-1
            else :
                sortedInputArray[mid] < elementToBeSearched
                low = mid+1

    #input value to be passed to the function
    sortedInputArray =30,40,60,80,90,95

    #test case 1, positive test case
    returnedValue = FindArrayElement (sortedInputArray,40)
    print ("the element to be searched is presenet at index ",returnedValue )

    #test case 2, positive test case
    returnedValue = FindArrayElement (sortedInputArray,80)
    print ("the element to be serached is presenet at index ",returnedValue )

    #test case 3, negative test case
    returnedValue = FindArrayElement (sortedInputArray,400)
    print ("the element to be serached is presenet at index ",returnedValue )












