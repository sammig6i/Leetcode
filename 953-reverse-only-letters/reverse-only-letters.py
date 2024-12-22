class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = [c for c in s if c.isalpha()]
        return "".join(c if not c.isalpha() else chars.pop() for c in s)