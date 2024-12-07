class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)

        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        
        res = []
        interval = []
        have = 0

        for key in sorted(mp):
            if not interval:
                interval.append(key)
            have += mp[key]
            if have == 0:
                interval.append(key)
                res.append(interval)
                interval = []
        
        return res


       