# def printMatrixDiagonally(inputNestedList):
#     for startDiagonalValue in range(0, len(inputNestedList) ):
#         rowIndex = startDiagonalValue
#         columnIndex = 0
#         while (rowIndex >= 0):
#             print(inputNestedList[rowIndex][columnIndex],end="")  # , inputNestedList[columnIndex])
#             rowIndex = rowIndex - 1
#             columnIndex = columnIndex + 1
#         print("")
#     print("columns length :",inputNestedList[0].__len__())
#
#
# matrix = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i',' j', 'k', 'l'], ['m',' n', 'o', 'p']]
# printMatrixDiagonally(matrix)


def printMatrixDiagonallyyy(inputNestedList):
    for startDiagonalValue in range(0, len(inputNestedList)):
        rowIndex = startDiagonalValue
        columnIndex = 0
        while (rowIndex >= 0):
            print(inputNestedList[rowIndex][columnIndex], end="")
            rowIndex = rowIndex - 1
            columnIndex = columnIndex + 1
        print("")
    columnLength = len(inputNestedList[0])
    print(columnLength)
    rowIndex = len(inputNestedList) - 1
    for startDiagonalValue in range(1, columnLength):
        columnIndex = startDiagonalValue
        rowIndex = len(inputNestedList) - 1
        while columnIndex <= columnLength - 1:
            print(inputNestedList[rowIndex][columnIndex], end="")
            rowIndex = rowIndex - 1
            columnIndex = columnIndex + 1
        print("\n")


matrix = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', ' j', 'k', 'l'], ['m', ' n', 'o', 'p']]
printMatrixDiagonallyyy(matrix)
printMatrixDiagonallyyy([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

