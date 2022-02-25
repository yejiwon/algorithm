class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix)
        if row == 1:
            return sum(matrix[0])

        for i in range(1,row):
            for j in range(col):
                if j == col-1 :
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1]) + matrix[i][j]
                elif j != 0 :
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1]) + matrix[i][j]
                else: 
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j+1]) + matrix[i][j]
        return min(matrix[row-1])