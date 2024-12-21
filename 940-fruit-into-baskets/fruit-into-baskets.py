class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        L = 0
        fruit1_lastIdx = 0
        fruit2_lastIdx = -1
        fruit1 = fruits[0]
        fruit2 = -1
        total = res = 0

        for R in range(len(fruits)):
            f = fruits[R]
            if f == fruit1:
                # total += 1
                fruit1_lastIdx = R
            elif f == fruit2 or fruit2 == -1:
                # total += 1
                fruit2_lastIdx = R
                fruit2 = f
            else:
                if fruit2_lastIdx == min(fruit1_lastIdx, fruit2_lastIdx):
                    fruit1_lastIdx, fruit2_lastIdx = fruit2_lastIdx, fruit1_lastIdx
                    fruit1, fruit2 = fruit2, fruit1
                # total -= (fruit1_lastIdx - L + 1)
                L = fruit1_lastIdx + 1
                fruit1 = f
                fruit1_lastIdx = R
            res = max(res, R - L + 1)
        return res
# 1,2,1,2,2,3
fruit1 = 3
fruit2 = 2
fruit1_lastIdx = 5
fruit2_lastIdx = 4

f = 3
total = 2
res = 5
L = 3