class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_occ = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }
        
        for s in text:
            if s in char_occ:
                char_occ[s] += 1
        
        char_occ["l"] //= 2
        char_occ["o"] //= 2
        
        return min(char_occ.values())
        
