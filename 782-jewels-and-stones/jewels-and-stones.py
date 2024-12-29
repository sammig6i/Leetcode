class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_cnt = Counter(stones)
        res = 0
        for j in jewels:
            if j in stones_cnt:
                res += stones_cnt[j]
        return res