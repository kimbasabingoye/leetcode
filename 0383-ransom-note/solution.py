class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_cnt = defaultdict(int)
        
        for s in ransomNote:
            char_cnt[s] += 1
        
        for s in magazine:
            if s in char_cnt:
                char_cnt[s] -= 1
        
        for v in char_cnt.values():
            if v > 0:
                return False
        
        return True
            
        
