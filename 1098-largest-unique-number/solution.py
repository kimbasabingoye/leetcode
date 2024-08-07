class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        occ_cnt = defaultdict(int)
        n = len(nums)
        
        for i in range(n):
            occ_cnt[nums[i]] += 1
        
        ans = -1
        
        for k, v in occ_cnt.items():
            if v == 1:
                ans = max(ans, k)
            
        return ans
