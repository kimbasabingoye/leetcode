class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        ans = set()
        for n in nums2:
            if n in s:
                ans.add(n)
        return ans
