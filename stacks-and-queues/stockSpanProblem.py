class StockSpanner:

    def __init__(self):
        self.allPrices = []
        self.stack = []
        self.lastIndex = 0
    def next(self, price: int) -> int:
        stack, allPrices = self.stack, self.allPrices
        # remove all elements from the stack which are actually smaller than or equal to current element
        while stack and allPrices[stack[-1]] <= price:
            stack.pop()
        allPrices.append(price) # add the price
        stack.append(len(allPrices) - 1) # obviously since this will be the last inces :)
        if len(stack) == 1: # i.e. only 1 single element exists which was just added
            return stack[-1] + 1
        else:
            return stack[-1] - stack[-2]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)