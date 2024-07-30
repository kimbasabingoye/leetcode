import math
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages = []
        n = len(nums)
        left = 0
        right = n-1
        ans = (nums[left] + nums[right])/2
        while left < right:
            cur = (nums[left] + nums[right])/2
            ans = min(cur, ans)
            
            left += 1
            right -= 1
        
        return ans
