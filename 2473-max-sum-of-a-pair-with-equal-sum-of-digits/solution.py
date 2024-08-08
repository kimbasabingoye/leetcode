class Solution:
    def sumdigits(self, num: int):
        ans = 0
        while num > 0:
            ans += num % 10
            num //= 10
        return ans

    def maximumSum(self, nums: List[int]) -> int:
        groups = defaultdict(int)
        ans = -1

        for num in nums:
            sum_digits = self.sumdigits(num)
            if sum_digits in groups:
                ans = max(ans, groups[sum_digits] + num)
            groups[sum_digits] = max(groups[sum_digits], num)
        
        return ans
