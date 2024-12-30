class Solution:
    def frequencySort(self, s: str) -> str:
        freq = [[] for _ in range(len(s) + 1)]
        res = []
        count = Counter(s)
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for char, freq in sorted_count:
            res.append(char * freq)
        return "".join(res)



        