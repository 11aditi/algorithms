# Python 3 program to count frequencies
# of array items
def countFreq(arr, n):
    # Mark all array elements as not visited
    visited = [False for i in range(n)]

    # Traverse through array elements
    # and count frequencies
    for i in range(n):

        # Skip this element if already
        # processed
        if (visited[i] == True):
            continue

        # Count frequency
        count = 1
        for j in range(i + 1, n, 1):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1

        print(arr[i], count)

    # Driver Code


if __name__ == '__main__':
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(arr)
    countFreq(arr, n)


def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("% d : % d" % (key, value))

    # Driver function


#if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

    CountFrequency(my_list)


