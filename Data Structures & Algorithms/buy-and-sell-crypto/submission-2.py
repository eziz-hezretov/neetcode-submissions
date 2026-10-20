class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_price = 101
        highest_profit = 0

        for current_price in prices:
            if current_price < lowest_price:
                lowest_price = current_price

            current_profit = current_price - lowest_price

            if current_profit >= highest_profit:
                highest_profit = current_profit

        return highest_profit