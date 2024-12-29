class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_count = Counter(arr)
        max_value = float("-inf")
        for n, c in num_count.items():
            if n == c:
                max_value = max(max_value, n)
        return -1 if max_value == float("-inf") else max_value