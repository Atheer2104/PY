def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp



def indexMinium(array, startIndex):
    minValue = array[startIndex]
    minIndex = startIndex

    for i in range(minIndex +1, len(array)):
        if (array[i] < minValue):
            minIndex = i
            minValue = array[i]

    return minIndex



def selectionSort(array):
    minimum = None
    for i in range(len(array)):
        minimum = indexMinium(array, i)
        swap(array, i, minimum)


array = [22, 11, 99, 88, 9, 7, 42]
selectionSort(array)
print(array)



