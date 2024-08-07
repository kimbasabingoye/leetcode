class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        loosers = defaultdict(int)
        
        for e in matches:
            players.add(e[0])
            players.add(e[1])
            
            loosers[e[1]] += 1
        
        answer_0 = []
        answer_1 = []
        
        for e in players:
            if e not in loosers:
                answer_0.append(e)
                
        for k, v in loosers.items():
            if v == 1:
                answer_1.append(k)
                
        answer_0.sort()
        answer_1.sort()
        
        return [answer_0, answer_1]
