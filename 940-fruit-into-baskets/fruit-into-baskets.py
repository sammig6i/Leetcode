class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # two baskets and each can hold only 1 type of fruit
        # no limit on the amount of fruit each basket can hold
        # starting from any tree, you must pick exactly one fruit from every tree, the picked fruits must fit in basket
        # find max length with only 2 unique values
        L = 0
        total = 0
        res = 0
        basket_count = defaultdict(int)
        for R in range(len(fruits)):
            basket_count[fruits[R]] += 1
            total += 1

            while len(basket_count) > 2:
                f = fruits[L]
                basket_count[f] -= 1
                total -= 1
                L += 1
                if not basket_count[f]:
                    del basket_count[f]

            res = max(res, total)
        return res
[1,2,3,2,2]
