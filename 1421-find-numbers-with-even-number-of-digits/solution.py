class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for e in nums:
            cnt = 0
            while e:
                e //= 10
                cnt += 1
            if  not (cnt & 1):
                ans += 1
        return ans
