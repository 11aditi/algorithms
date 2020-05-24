class Node :
    def __init__(self,inputData):
        self.inputDatainConstructor = inputData
        self.next = None
        #self.test="Hello Mr How are you"
        print (" the constructor of class node executed", self.inputDatainConstructor)



#A new class LinkedList started
class LinkedList :
    def __init__(self):
        self.head = None

    # def printLinkedList(self,firstNodeOfLinkList):
    #     temp = firstNodeOfLinkList
    #     while (temp):
    #         print(temp.inputDatainConstructor)
    #         temp = temp.next

    def findLengthOfLinkList (self,firstNodeOfLinkList):
        temp = firstNodeOfLinkList
        count = 1
        while (temp) :
            if temp.next == None :
                break
            else :
                temp=temp.next
                count = count+1
        return count

    def printMidNode(self,firstNodeOfLinkList,length):
        temp = firstNodeOfLinkList
        count = 1
        middle = length//2
        while (middle>count) :
            temp = temp.next
            count  = count+1
        print ("The value at middle node is:", temp.inputDatainConstructor)

    def printMiddleNodeLC(self,firstNode):
      slow = firstNode
      fast = firstNode
      while (fast) :
        slow = slow.next
        fast = fast.next.next
      print ("The value at middle node is:",slow.inputDatainConstructor )

    def findLoop(self,Node1):
        slow= Node1
        fast = Node1
        while (fast):
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                print ("Loop exists")
                break
            else :
                print ('Loop not found')


if __name__=='__main__':
    refVariable = LinkedList()
    refVariable.head = Node(("Aditi","Sep","Shivin","dhwani",))
    secondNode = Node(2)
    thirdNode = Node(3)
    fourthNode = Node(4)
    fifthNode = Node(5)
    sixthNode = Node(6)

    refVariable.head.next=secondNode
    secondNode.next = thirdNode
    thirdNode.next = fourthNode
    fourthNode.next = fifthNode
    fifthNode.next = sixthNode
    sixthNode.next = None
    #print(thirdNode.test)

    #refVariable.printLinkedList(refVariable.head)
    #length=refVariable.findLengthOfLinkList(refVariable.head)
    #print ("The length of linked list is :", length)


    #refVariable.printMidNode(refVariable.head,length)
    #refVariable.printMiddleNodeLC(refVariable.head)
    refVariable.findLoop(refVariable.head)




