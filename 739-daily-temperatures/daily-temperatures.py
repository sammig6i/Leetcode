class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair (index, temp)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                lastIndex, lastTemp = stack.pop()
                res[lastIndex] = i - lastIndex
            stack.append((i, t))
        return res

