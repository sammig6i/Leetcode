class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        L, R = 0, COLS - 1
        while L <= R:
            M = L + ((R - L) // 2)
            if target > matrix[row][M]:
                L = M + 1
            elif target < matrix[row][M]:
                R = M - 1
            else:
                return True
        return False

