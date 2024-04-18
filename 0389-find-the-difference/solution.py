class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ""
        s1 = sorted(s)
        t1 = sorted(t)

        i = len(s1)

        for k in range(i):
            if s1[k] != t1[k]:
                res += t1[k]
                return res
        
        res += t1[-1]
        return res

        


        
