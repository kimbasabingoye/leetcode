class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        n = len(pick)
        d = {}
        for e in pick:
            key = str(e[0]) + str(e[1])
            if key in d:
                d[key] += 1
            else:
                d[key] = 1
        
        winner = set() 
        for key, value in d.items():
            i = int(key[0])
            if value >= i+1:
                winner.add(i)
            
        return len(winner)
