class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        l = 0
        
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            output = max(output, prices[r] - prices[l])

            
        return output