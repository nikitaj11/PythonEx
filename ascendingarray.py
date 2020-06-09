array = [1,2,5,5,6,6,3]
temp = 0
def ascendingarray():
    print("Elements of original array:",array)
    for i in range(0,len(array)):
        print(array[i])

    for i in range(0,len(array)):
        for j in range(i, len(array)):
            if(array[i] > array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    print("Elements of array in ascending order:",array)
    for i in range(0,len(array)):
        print(array[i])          

ascendingarray() 

