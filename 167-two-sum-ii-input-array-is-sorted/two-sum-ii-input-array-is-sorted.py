class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            sumLR = numbers[R] + numbers[L]
            if sumLR == target:
                return [L + 1, R + 1]
            elif sumLR < target:
                L += 1
            else:
                R -= 1
        