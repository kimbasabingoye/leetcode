class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        occ_pos = defaultdict(list)
        n = len(cards)

        for i in range(n):
            occ_pos[cards[i]].append(i)
            
        ans = n+1
        for k, v in occ_pos.items():
            for l in range(len(v)-1):
                ans = min(ans, v[l+1]-v[l]+1)
    
        if ans == n+1 :
            return -1
        return ans if ans < n+1 else -1
