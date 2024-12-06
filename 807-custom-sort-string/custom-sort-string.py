class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # order - find all occurences in s and place in order
        if not order or not s:
            return s
        
        count = defaultdict(int)

        for c in s:
            count[c] += 1
        
        res = []
        for c in order:
            if c in count:
                res.append(c * count[c])
                del count[c]
        
        for c, count in count.items():
            res.append(c * count)

        return "".join(res)
                
# cba
# aaabbbccc
# res = cccbbbaaa