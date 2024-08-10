class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = defaultdict(int)
        ans = -1

        for e in arr:
            cnt[e] += 1

        for k, v in cnt.items():
            if k == v:
                ans = max(ans, k)

        return ans
