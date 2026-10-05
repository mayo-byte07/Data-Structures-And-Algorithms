class Solution(object):
    def maxProfit(self, prices, fee):
        free = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            free, hold = (
                max(free, hold + prices[i] - fee), 
                max(hold, free - prices[i])
            )
        return free