class Solution:
    def frequencySort(self, s: str) -> str:
        freq = [[] for _ in range(len(s) + 1)]
        res = []
        count = Counter(s)
        for char, count in count.items():
            freq[count].append(char * count)
        
        for i in range(len(freq) - 1, -1, -1):
            for c in freq[i]:
                res.append(c)
        return "".join(res)



        