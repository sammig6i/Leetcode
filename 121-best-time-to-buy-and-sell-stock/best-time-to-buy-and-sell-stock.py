class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L = 0

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            profit = max(profit, prices[R] - prices[L])
        return profit