class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        diagonal = []
        res = []
        
        for r in range(rows):
            for c in range(cols):
                if r == rows - 1 or c == cols - 1:
                    continue
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        
        return True


                    

                    