class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True