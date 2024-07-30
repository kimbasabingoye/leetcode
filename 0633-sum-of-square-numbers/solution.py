import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))
        s = 0
        while i <= j:
            s = i*i + j*j
            if s == c:
                return True
            elif s < c:
                i += 1                
            else:
                j -= 1

        return False
