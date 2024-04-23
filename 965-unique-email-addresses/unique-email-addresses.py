class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local = ""
            i = 0
            while email[i] not in ["+", "@"]:
                if email[i] != ".":
                    local += email[i]
                i += 1
            while email[i] != "@":
                i += 1
            domain = email[i + 1:]
            unique.add((local,domain))
        return len(unique)
        
                   
                    
                
            