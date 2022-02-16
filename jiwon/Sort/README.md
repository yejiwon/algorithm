# 정렬

## Bubble sort (stable)
- 뒤에서부터 정렬됨
- 복잡도
  - Best: O(n) time | O(1) space
  - Avg: O(n^2) time | O(1) space
  - Worst: O(n^2) time | O(1) space
```Python
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
```

## Insertion sort (stable)

## Merge sort (stable)

## Radix sort (stable)

## Counting sort (stable)

## Selection sort

## Quick sort

## Heap sort

## Radix sort