class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = nums + nums
        ans = curr = total = 0
        n = len(nums)

        for i in range(n):
            if nums[i]:
                total += 1
        
        for i in range(total):
            if not nums[i]:
                curr += 1

        ans = curr
        
        for i in range(total, 2*n):
            if not arr[i - total]:
                curr -= 1
            if not arr[i]:
                curr += 1
                
            ans = min(ans, curr)
        
        return ans
