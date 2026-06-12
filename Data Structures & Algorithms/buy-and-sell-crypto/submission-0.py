class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_p_index = 0
        highest_profit = 0 
        for i, p in enumerate(prices):
            if p < prices[lowest_p_index]:
                lowest_p_index = i
            current_profit = p - prices[lowest_p_index]
            if current_profit > highest_profit:
                highest_profit = current_profit
        return highest_profit

