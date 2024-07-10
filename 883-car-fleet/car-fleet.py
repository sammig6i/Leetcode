class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]

        pairs.sort()
        stack = []

        for p, s in pairs[::-1]:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)