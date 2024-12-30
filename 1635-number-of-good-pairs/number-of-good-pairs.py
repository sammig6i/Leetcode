class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        freq = Counter(nums)
        for n, c in freq.items():
            pairs += c * (c - 1) // 2
        return pairs