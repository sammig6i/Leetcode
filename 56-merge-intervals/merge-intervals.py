class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_start = max(interval[0] for interval in intervals)
        mp = [0] * (max_start + 1)

        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])
        
        res = []
        interval_start = -1
        have = -1

        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
            have = max(mp[i] - 1, have)
            if have == i:
                res.append([interval_start, have])
                interval_start = -1
                have = -1
        
        if interval_start != -1:
            res.append([interval_start, have])
        
        return res

       