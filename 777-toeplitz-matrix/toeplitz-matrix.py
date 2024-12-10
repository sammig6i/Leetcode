class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        def is_diagonal(row, col):
            val = matrix[row][col]

            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != val:
                    return False
                
                row += 1
                col += 1
            return True
        
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        for row in range(rows):
            if not is_diagonal(row, 0):
                return False
        
        for col in range(cols):
            if not is_diagonal(0, col):
                return False
        
        return True

