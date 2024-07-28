class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_s = 0
        sum_d = 0
        for n in nums:
            if n > 9:
                sum_d += n
            else:
                sum_s += n

        if sum_d != sum_s:
            return True
        return False
