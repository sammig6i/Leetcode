class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1
        
        return sum(n for n in mp if mp[n] == 1)