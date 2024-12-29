class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        res = 0
        stones_cnt = Counter(stones)

        for j in jewels:
            if j in stones_cnt:
                res += stones_cnt[j]
        return res