class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        n = len(nums)
        right = n - 1
        
        ans = [0]*n
        i = n - 1
        
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
                
            ans[i] = square * square
            i -= 1
                    
                
        return ans
