class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = Counter(arr)

        freq_set = set()
        for n, freq in freq_map.items():
            if freq in freq_set:
                return False
            freq_set.add(freq)
        return True
