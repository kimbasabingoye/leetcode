class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jls = set(jewels)
        ans = 0
        
        for s in stones:
            if s in jls:
                ans += 1
                
        return ans
        
