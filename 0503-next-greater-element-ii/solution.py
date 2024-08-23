class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums
        n = len(nums)

        ans = [-1] * (n)

        for i in range(n):
            j = i + 1
            while j <= (i + n - 1) and nums2[j] <= nums2[i]:
                j += 1
            
            if j <= n + i - 1:
                ans[i] = nums2[j]
                
        
        return ans
