def arr(list):

    for i in range(0,len(list)):
        check = [False for i in range (0,4)]
        if check[i]== True :
             continue

        isMonotonic = True
        for j in range(i+1, 4) :
          if list[i]<= list[j]:
              continue
          else :
              isMonotonic = False
              break
         #check[j] = True


    if isMonotonic==True :
                print ("Array is monotonic")






def isArrayMonotonous(inputParameterList):

    isMonotonic=True;
    #this loop is to check if next element is always greater then the previous element
    for i in range(0,len(inputParameterList)-1):
        print(inputParameterList[i])
        if(inputParameterList[i] >inputParameterList[i+1]):
             continue
        else:
            isMonotonic=False
            break

    if(isMonotonic==False):
        # this loop is to check if next element is always smaller then the previous element
        isMonotonic = True
        for i in range(0, len(inputParameterList)-1):
            if (inputParameterList[i] < inputParameterList[i + 1]):
                continue
            else:
                isMonotonic = False
                break

    if isMonotonic==True :

                print ("Array is monotonic")
    else:
        print("Array is not monotonic")

value = [1,2,3,4]
value1 = [1,3,2,5]
isArrayMonotonous(value)
isArrayMonotonous(value1)






