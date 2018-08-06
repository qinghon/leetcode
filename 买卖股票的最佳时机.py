class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        profit=0
        for price in range(1,len(prices)):
            if prices[price]>=prices[price-1]:
                profit+=(prices[price]-prices[price-1])
            else:
                continue
        return profit

