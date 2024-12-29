class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_count = Counter(arr)
        max_value = float("-inf")
        max_value = max((n for n, c in num_count.items() if n == c), default=None)
        return -1 if not max_value else max_value