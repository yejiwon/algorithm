class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [[1, 1, 1, 1, 1], [5, 4, 3, 2, 1]]
        
        if n > 2:
            for idx in range(2, n):
                point = arr[idx-1]
                arr.append([sum(point), sum(point[1:]), sum(point[2:]), sum(point[3:]), 1])
        return sum(arr[n-1])