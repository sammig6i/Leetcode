class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = set()

        for e in emails:
            i = 0
            local = ""
            while e[i] not in ("@", "+"):
                if e[i] != ".":
                    local += e[i]
                i += 1
            
            while e[i] != "@":
                i += 1
            domain = e[i + 1:]
            valid.add((local, domain))
        return len(valid)

        


            

