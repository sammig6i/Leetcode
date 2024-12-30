class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        pairs = 0
        for n, c in freq.items():
            pairs += c * (c - 1) // 2
        return pairs