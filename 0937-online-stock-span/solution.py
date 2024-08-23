class StockSpanner:

    def __init__(self):
        self.stocks = []
        

    def next(self, price: int) -> int:
        ans = 1
        while self.stocks and self.stocks[-1][0] <= price:
            ans += self.stocks.pop()[1]

        self.stocks.append([price, ans])
        return ans 
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
