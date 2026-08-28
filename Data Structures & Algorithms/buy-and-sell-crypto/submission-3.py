class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1

        max_profit = 0

        while l < r and r < len(prices) and l < len(prices): 

            current_profit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                r += 1
                
                max_profit = max(current_profit, max_profit)
    
            else:
                l = r
                r += 1

            

        return max_profit
            