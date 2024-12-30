class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = [[] for _ in range(len(arr) + 1)]

        count = Counter(arr)
        
        for n, c in count.items():
            freq[c].append(n)
        
        for lst in freq:
            if len(lst) > 1:
                return False
        return True