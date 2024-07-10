class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top += 1
            elif target < matrix[row][0]:
                bot -= 1
            else:
                break
        
        L, R = 0, COLS - 1

        while L <= R:
            m = L + (R - L) // 2

            if matrix[row][m] > target:
                R -= 1
            elif matrix[row][m] < target:
                L += 1
            else:
                return True
        return False