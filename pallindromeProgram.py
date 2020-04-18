def isStringPalindrome(inputString):
    if inputString == inputString[ : :-1] :
        print ("It is a Pallindrome")
    else :
         print ("It is not a Pallindrome")


isStringPalindrome("aba")
isStringPalindrome("abba")
isStringPalindrome("abc")



def isPalindromeUsingLoop(inputStringString):
    low=0
    high=len(inputStringString)-1
    palindromeFlagIndicator=True;
    while(low<high):
        if(inputStringString[low]==inputStringString[high]):
            low=low+1
            high=high-1
            continue
        else:
            print("Given string sis not palindrome",inputStringString)
            palindromeFlagIndicator=False
            break
    if(palindromeFlagIndicator):
        print("string is palindrome",inputStringString)


print("=======executing function isPalindromeUsingLoop()")
isPalindromeUsingLoop("aba")
isPalindromeUsingLoop("abba")
isPalindromeUsingLoop("abc")

def isPalindromeRecursion(inputStringString, low, high):
    #base condition
    if(low==high):
        return True
    if(inputStringString[low]!=inputStringString[high]):
        return False
    else:
        callRecursive= isPalindromeRecursion(inputStringString,low+1,high-1)
        return  callRecursive

def callingFunction(inputStringString):
    return isPalindromeRecursion(inputStringString,0,len(inputStringString)-1)


# print("=======executing function isPalindromeRecursion()======================")
# result=callingFunction("abcxcba")
# print("=======executing function isPalindromeRecursion()",result)

# result=callingFunction("abac")
# print("=======executing function isPalindromeRecursion()",result)

# result=callingFunction("abaca")
# print("=======executing function isPalindromeRecursion()",result)
#
result=callingFunction("ababa")
print("=======executing function isPalindromeRecursion()",result)