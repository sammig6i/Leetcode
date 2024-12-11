class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        num_seen = False
        decimal_seen = False

        i = 0
        if s[i] in ("+", "-"):
            i += 1
        
        while i < len(s):
            c = s[i]

            if c.isdigit():
                num_seen = True
            if c.isalpha():
                if c in ("e", "E"):
                    return num_seen and self.is_valid_integer(s[i + 1:])
                else:
                    return False
            if c in ("+", "-"):
                return False
            if c == ".":
                if decimal_seen:
                    return False
                else:
                    decimal_seen = True
            
            i += 1
        return num_seen
    
    def is_valid_integer(self, s):
        if not s:
            return False
        
        num_seen = False

        i = 0
        if s[i] in ("+", "-"):
            i += 1
        
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num_seen = True
            if c.isalpha():
                return False
            if c in ("+", "-"):
                return False
            if c == ".":
                return False
            i += 1
        
        return num_seen