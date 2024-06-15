class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for account in accounts:
            w = sum(account)
            if w > wealth:
                wealth = w
        return wealth
        
