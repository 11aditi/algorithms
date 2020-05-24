from collections import deque


def findNGE(array):
    stack = deque()
    stack.append(array[0])

    for i in range(1, len(array)):
        peek = stack[-1] ##this returns top most  value of stack
        if array[i] < peek:
            stack.append(array[i])
        else:
            peek= stack[-1]
            while peek < array[i] and len(stack)>0:
                top = stack.pop()
                print("NGE for ", top, " is ", array[i])
                if len(stack)>0 :
                 peek=stack[-1]
            stack.append(array[i])  # outside while loop

    while stack.__len__() != 0:
        top = stack.pop()
        print("NGE for ", top, " is Null")


# A = [98, 77, 65, 82]
# print(findNGE(A))
#
# B = [8, 77, 65, 82]
# print(findNGE(B))
#
# C = [8,108, 77, 65, 82,143]
# print(findNGE(C))

D= [62,10,27,38,97,8]
print(findNGE(D))