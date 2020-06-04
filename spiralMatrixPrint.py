def spiralMatrixPrint(endRowIndex,endColIndex,matrix) :
    startRowIndex = 0
    startColIndex = 0
    while (startRowIndex < endRowIndex and startColIndex < endColIndex):

        for i in range (startColIndex,endColIndex+1):
            print(matrix[startRowIndex][i],end =' ')
        #print(" ")

        startRowIndex= startRowIndex +1

        for i in range (startRowIndex,endRowIndex+1):
            print (matrix[i][endColIndex],end = ' ')
        #print (" ")

        endColIndex= endColIndex -1

        for i in range (endColIndex,startColIndex-1,-1):
            print(matrix[endRowIndex][i],end =' ')

        endRowIndex= endRowIndex-1

        for i in range (endRowIndex,startRowIndex-1,-1):
            print(matrix[i][startColIndex],end =' ')

        startColIndex+=1

matrix = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t']]
spiralMatrixPrint(3,4,matrix)