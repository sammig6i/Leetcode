class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        freq = set()
        
        for n, c in count.items():
            if c in freq:
                return False
            freq.add(c)
        return True