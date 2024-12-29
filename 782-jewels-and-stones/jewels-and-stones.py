class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        stones_cnt = Counter(stones)
        res += sum(stones_cnt[j] for j in jewels if j in jewels)
        return res