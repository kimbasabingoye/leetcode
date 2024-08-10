class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0

        for e in nums:
            cnt[e] += 1

        for k, v  in cnt.items():
            if v == 1:
                ans += k
        
        return ans
        
