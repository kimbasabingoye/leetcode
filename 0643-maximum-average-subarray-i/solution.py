class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0.0
        for i in range(k):
            curr += nums[i]
        ans = curr
        #print(ans)
        for i in range(k, len(nums)):
            curr += nums[i]
            curr -= nums[i-k]
            if curr > ans:
                ans = curr
        return ans/k
        
