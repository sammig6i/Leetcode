class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        res = []

        arr = []
        for v in original:
            arr.append(v)
            if len(arr) == n:
                res.append(arr)
                arr = []
        
        return res

