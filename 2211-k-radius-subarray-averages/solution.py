class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        p_sum = [0] * (n+1)
        
        for i in range(n):
            p_sum[i+1] = p_sum[i] + nums[i]
        
        avgs = []
        
        for i in range(n):
            if i - k >= 0 and i + k < n:
                avgs.append((p_sum[i+k+1] - p_sum[i-k]) // (2*k+1))
            else:
                avgs.append(-1)
                
        
        return avgs
