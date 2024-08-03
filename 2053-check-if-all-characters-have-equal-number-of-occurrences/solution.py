class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        n = len(s)

        for i in range(n):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        
        v = d[s[0]]
        for val in d.values():
            if val != v:
                return False
        return True
         
