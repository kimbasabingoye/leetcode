class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for p in details:
            if int(p[11:13]) > 60:
                ans += 1
        return ans
        
