class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans  = 0
        seen = set()
        left = right = 0
        n = len(s)
        
        for right in range(n):
            curr = s[right]
            
            if curr not in seen:
                seen.add(curr)
            else:
                while s[left] != curr:
                    seen.remove(s[left])
                    left += 1
                left += 1
            
            ans = max(ans, right - left + 1)
    
        return ans 
