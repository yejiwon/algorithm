def bubbleSort(array):
    for i in range(len(array)-1, 0, -1):
        isSorted = True
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                isSorted = False
        if isSorted:
            return array
    return array
