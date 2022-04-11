# 정렬
- https://gmlwjd9405.github.io/tags#sort

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
- 요소를 기존의 정렬된 요소 사이의 올바른 자리를 찾아 삽입
- 복잡도
  - Best: O(n) time | O(1) space
  - Avg: O(n^2) time | O(1) space
  - Worst: O(n^2) time | O(1) space
    - 자료가 역순인 경우
```Python
def insertionSort(array):
	for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
			j -= 1
	return array
```

## Merge sort (stable)

## Radix sort (stable)

## Counting sort (stable)

## Selection sort
- in-place sorting
- 첫 번째 자료를 두 번째 자료부터 마지막 자료까지 차례대로 비교하여 가장 작은 값을 찾아 첫 번째에 놓고, 두 번째 자료를 세 번째 자료부터 마지막 자료까지와 차례대로 비교하여 그 중 가장 작은 값을 찾아 두 번째 위치에 놓는 과정을 반복하는 방법
- 복잡도
  - Best: O(n^2) time | O(1) space
  - Avg: O(n^2) time | O(1) space
  - Worst: O(n^2) time | O(1) space
- ![image](https://user-images.githubusercontent.com/95209913/159968573-ad21d104-397e-49be-b2d9-d103ef6a565f.png)
```Python
def selectionSort(array):
    for currentIdx in range(len(array)-1):
		minIdx = currentIdx
		for j in range(currentIdx+1, len(array)):
			if array[j] < array[minIdx]:
				minIdx = j
		array[currentIdx], array[minIdx] = array[minIdx], array[currentIdx]
	
	return array
```

## Quick sort
- 매우 빠른 정렬 🏃‍♀️
- 하나의 리스트를 피벗(pivot)을 기준으로 두 개의 비균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법
- 복잡도
  - Best: O(nlogn) time | O(logn) space
  - Avg: O(nlogn) time | O(logn) space
  - Worst: O(n^2) time | O(logn) space
    - **리스트가 계속 불균형하게 나누어지는 경우 = 이미 정렬된 리스트인 경우**
```Python

```

## Heap sort

## Radix sort