class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        s = []
        n = len(nums)
        
        for start in range(n):
            su = 0
            for end in range(start, n):
                su += nums[end]
                s.append(su)

        s.sort()
        
        return sum(s[left-1:right])%(10**9+7)

        
