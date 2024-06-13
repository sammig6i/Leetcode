class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (temp, index)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                lastIndex = stack[-1][1]
                res[lastIndex] += (i - lastIndex)
                stack.pop()
            stack.append((t, i))
        return res
