class Solution(object):
    def maxProfit(self, prices):
        
        """
        make an algoirthm with 2 pointers in a while loop,
        make an l variable which is buy, and a r variable which is sell.
        
        """
        l, r = 0, 1
        max_p = 0
        while(r < len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                #check whether the price for max_p is greater than the profit, to update max profit
                max_p = max(max_p, profit)
            else:
                l = r
            r += 1
        return max_p
    