class Solution:
    def isNumber(self, s: str) -> bool:
        decimal_used = False
        digit_seen = False

        i = 0
        if s[i] in ("+", "-"):
            i += 1
        
        while i < len(s):
            c = s[i]

            if c.isalpha():
                if c not in ("e", "E"):
                    return False
                else:
                    return digit_seen and self.is_valid_integer(s[i + 1:])
            elif c == ".":
                if decimal_used:
                    return False
                else:
                    decimal_used = True
            elif c in ("+", "-"):
                return False
            else:
                digit_seen = True
            
            i += 1

        return digit_seen

    def is_valid_integer(self, s):
        if not s:
            return False
        
        digit_seen = False

        i = 0
        if s[i] in ("+", "-"):
            i += 1
        
        while i < len(s):
            c = s[i]

            if not c.isdigit():
                return False
            else:
                digit_seen = True
            
            i += 1

        return digit_seen

    -123.456e789
    +6e-1