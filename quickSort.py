def quickSort(arr, low, high):
    
    #If the arr is sufficiently long
    if low < high:

        #Find the pivot so small elements are on the left, big on the right
        pivot = partition(arr, low, high)

        #Recursive call on the left
        quickSort(arr, low, pivot-1)

        #Recursive call on the right
        quickSort(arr, pivot+1, high)

def partition(arr, low, high):

    #Set the pivot as the rightmost element
    pivot = arr[high]

    #Points to greater element
    i = low - 1

    #Compare each element to the point
    for j in range(low, high):

        #If the element is smaller than the pivot, swap it with i
        if arr[j] <= pivot:

            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    #Finally, swap the pivot with the greater element i
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1


#Test code
array = [10, 7, 8, 9, 1, 5]
n = len(array)

quickSort(array, 0, n-1)
print(array)