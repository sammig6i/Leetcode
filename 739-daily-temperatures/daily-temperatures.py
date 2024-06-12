class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                lastIndex = stack[-1][1]
                res[lastIndex] += (i - lastIndex)
                stack.pop()
            stack.append([t, i])
        return res
                
            

    
        




        

