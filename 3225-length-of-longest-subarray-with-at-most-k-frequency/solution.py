class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # initialize an empty dict to count elem freq
        # set left = 0 and right = 0
        # iterate trough nums
        #   check if the freq of elem i is <= k
        #       if so increment elem i count
        #       else move left to the elem after an occurrence of elem i
        #   update ans as max btw curr and prev=right-left+1

        cnt = defaultdict(int)
        left = right = ans = 0
        n = len(nums)

        for right in range(n):
            cnt[nums[right]] += 1
            
            while cnt[nums[right]] > k:
                cnt[nums[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
