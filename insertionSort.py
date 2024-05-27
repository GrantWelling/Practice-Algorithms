def insertionSort(arr):

    #Initiate sorting at second index
    for i in range(1, len(arr)):

        #Store current index as value
        value = arr[i]

        j = i-1

        #Keep scooting the list until value is in the correct index
        while j >= 0 and value < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        #Assign value in the correct location
        arr[j+1] = value

#Test code
arr1 = [33, 21, 1, 50, 100]

arr2 = [99999, 0, 999, 9999, 9, 99]

insertionSort(arr1)

insertionSort(arr2)

print(arr1)
print()
print(arr2)