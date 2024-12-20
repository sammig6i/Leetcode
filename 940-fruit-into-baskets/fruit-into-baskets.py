class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        L = 0

        for R in range(len(fruits)):
            count[fruits[R]] += 1

            if len(count) > 2:
                count[fruits[L]] -= 1
                if count[fruits[L]] == 0:
                    del count[fruits[L]]
                L += 1
        
        return len(fruits) - L