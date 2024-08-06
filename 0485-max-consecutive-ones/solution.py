class Solution:
        
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        cnt = 0
        for i in range(n):
            if nums[i] == 1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0

        return max(ans, cnt)
                
            
            
