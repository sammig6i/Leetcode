class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for start, end in intervals:
            if not res:
                res.append([start, end])
            else:
                last_end = res[-1][1]
                if start <= last_end:
                    res[-1][1] = max(last_end, end)
                else:
                    res.append([start, end])
        return res