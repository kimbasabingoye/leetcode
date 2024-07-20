class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        i = x
        j = y
        turn = 0
        while i >= 1 and j >= 4:
            i -= 1
            j -= 4
            turn += 1
        if turn % 2 == 0:
            return "Bob"
        return "Alice" 
        
