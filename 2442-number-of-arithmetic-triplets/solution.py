class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = 0
        n = len(nums)
        for num in nums:
            if num+diff in nums and num+2*diff in nums:
                cnt += 1
        return cnt
