class Solution:
    def isHappy(self, n: int) -> bool:
        curr = n
        seen = set()

        seen.add(curr)
        while True:
            digits = [ int(x)*int(x) for x in str(curr)]
            curr = sum(digits)
            if curr == 1:
                return True
            if curr in seen:
                return False
            seen.add(curr)
            
