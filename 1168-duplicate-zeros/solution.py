class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        nums = [0]*n
        i = j = 0
        
        while i < n and j < n:
            nums[j] = arr[i]
            j += 1
            
            if arr[i] == 0 and j < n:
                nums[j] = arr[i]
                j += 1
            
            i+= 1
        for i in range(n):
            arr[i] = nums[i]
                
        
        
