from collections import defaultdict
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_res = 0
        
        for n in nums:
            xor_res ^= n
            
        return xor_res
