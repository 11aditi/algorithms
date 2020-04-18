
# A:Apple, Avocado
# B : Banana, Berry
def countElements(inpFruits):
    dict = {}
    maxCount=0
    for ele in inpFruits:
        firstChar = ele[0:1]
        if firstChar in dict:
            dict[firstChar].append(ele)
            currentListCount= len(dict[firstChar])
            if(currentListCount> maxCount):
                maxCount=currentListCount
        else:
            maxCount=1
            dict[firstChar] = [ele]
    print(dict,maxCount)


values = ["Apple", "Banana", "Berry"]
countElements(values)


def findElement(inpParameter,elementToBeSearched) :
    found = {}
    for element in inpParameter :
        found.setdefault(element,0)

    if elementToBeSearched in found.keys():
        print (elementToBeSearched,"is present in given array",inpParameter)
        return True
    else :
        print(elementToBeSearched , "is not present in given array",inpParameter)
        return False


value = 12,23,45
returnedValue=findElement(value,112)
print("value returned by the function is:",returnedValue)

returnedValue=findElement(value,12)
print("value returned by the function is:",returnedValue)

returnedValue=findElement(value,45)
print("value returned by the function is:",returnedValue)





