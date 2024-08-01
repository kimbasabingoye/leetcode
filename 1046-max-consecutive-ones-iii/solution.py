class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        z_cnt = 0
        ans = 0

        for right in range(n):
            if nums[right] == 0:
                z_cnt += 1
            
            while z_cnt > k:
                if nums[left] == 0:
                    z_cnt -= 1
                left += 1

            ans = max(ans, right-left+1)

        return ans
