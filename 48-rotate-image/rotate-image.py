class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                rotated[c][n - 1 - r] = matrix[r][c]
        
        for r in range(n):
            for c in range(n):
                matrix[r][c] = rotated[r][c]