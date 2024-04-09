class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            res.append(n)
        
        res = res + nums

        return res