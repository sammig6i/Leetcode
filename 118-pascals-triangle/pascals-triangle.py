class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for r in range(len(res[-1]) + 1):
                row.append(temp[r] + temp[r + 1])
            res.append(row)
        
        return res
