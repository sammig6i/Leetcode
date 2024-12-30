class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        count = Counter(s)
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for c, freq in sorted_count:
            res.append(c * freq)
        return "".join(res)



        