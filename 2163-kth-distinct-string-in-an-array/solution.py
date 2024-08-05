class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = defaultdict(int)

        for s in arr:
            d[s] += 1

        cnt = 0
        for s in arr:
            if d[s] == 1:
                cnt += 1
                if cnt == k:
                    return s
        return ""
        
