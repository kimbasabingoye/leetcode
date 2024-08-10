class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = defaultdict(int)

        for e in arr:
            cnt[e] += 1
        
        return len(set(cnt.values())) == len(cnt)
        
