class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix = cur = nums[0]
        
        for i in range(1, len(nums)):
            cur += nums[i]
            min_prefix = min(min_prefix, cur)
        
        if min_prefix >= 1:
            return 1
        return abs(min_prefix)+1
