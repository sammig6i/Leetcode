class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R

        while L <= R:
            m = L + ((R - L) // 2)
            hours = 0
            for p in piles:
                hours += ((m + p - 1) // m)
            
            if hours <= h:
                res = min(res, m)
                R = m - 1
            elif hours > h:
                L = m + 1
        return res
