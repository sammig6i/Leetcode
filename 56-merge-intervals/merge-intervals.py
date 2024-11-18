class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for start, end in intervals:
            if res:
                last_end = res[-1][1]
                if start <= last_end:
                    if end <= last_end:
                        continue
                    else:
                        res[-1][1] = end
                else:
                    res.append([start, end])
            else:
                res.append([start, end])
        return res