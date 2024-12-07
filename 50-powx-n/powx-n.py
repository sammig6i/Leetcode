class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.res = self.helper(x, abs(n))
        return self.res if n >= 0 else 1 / self.res
        

    def helper(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        self.res = self.helper(x, n // 2)
        self.res *= self.res
        return x * self.res if n % 2 else self.res
        
    