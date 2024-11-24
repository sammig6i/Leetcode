class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for start, end in intervals:
            d[start] += 1
            d[end] -= 1
        res = []
        interval = []
        have = 0

        for i in sorted(d):
            if not interval:
                interval.append(i)
            have += d[i]
            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []
                have = 0
        return res