class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max=0
        price_min=prices[0]

        for i in range(1,len(prices)):
            if prices[i] < price_min:
                price_min=prices[i]
            else:
                profit_today=prices[i]-price_min
                if profit_today>profit_max:
                    profit_max=profit_today
        return profit_max