class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)

        cnt = collections.Counter(s)
        
        m = max(cnt.values())

        bucket = [[] for _ in range(m+1)]
        for k, v in cnt.items():
            bucket[v].append(k)

        ans = []
        for i in range(m, 0, -1):
            for c in bucket[i]:
                ans.append(c*i)
        
        return "".join(ans)
