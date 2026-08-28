class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProf = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                maxProf = max(maxProf, 0)
                l = r
                r += 1
            else:
                maxProf = max(maxProf, profit)
                r += 1
            
        return maxProf
            
            
         