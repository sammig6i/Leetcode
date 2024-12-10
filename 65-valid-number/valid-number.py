class Solution:
    def isNumber(self, s: str) -> bool:
        # integer followed by exponent
        # decimal number followed by exponent
        # - or + followed by integers or decimals
        # digits followed by a dot
        # digits followed by a dot followed by digits
        # a dot followed by digits
        # integers after an exponent 'e' or 'E'

        num_seen = False
        decimal_seen = False

        i = 0
        if s[i] in ("+", "-"):
            i += 1
        
        while i < len(s):
            c = s[i]
            if c.isalpha():
                if c in ("e", "E"):
                    return num_seen and self.is_valid_integer(s[i + 1:])
                else:
                    return False
            if c.isdigit():
                num_seen = True
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
        if not len(s):
            return False
        
        num_seen = False
        i = 0
        if s[i] in ("+", "-"):
            i += 1

        while i < len(s):
            c = s[i]
            if not c.isdigit():
                return False
            else:
                num_seen = True
            i += 1
        
        return num_seen