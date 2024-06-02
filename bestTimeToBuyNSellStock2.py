class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
        On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
        Find and return the maximum profit you can achieve.
        
        Example 1:
        Input: prices = [7,1,5,3,6,4]
        Output: 7
        Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
        Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
        Total profit is 4 + 3 = 7.
        
        Example 2:
        Input: prices = [1,2,3,4,5]
        Output: 4
        Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
        Total profit is 4.
        
        Example 3:
        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

        My approach is to use two pointers
        """
        i = 0
        profit = 0
        total_profit = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                if (prices[j] - prices[i]) > profit:
                    profit = profit[j] - profit[i]
                else:
                    i = j
                    total_profit += profit
                    profit = 0
            else:
                i = j
                total_profit += profit
                profit = 0
        total_profit = total_profit + profit if profit > 0 else total_profit
        return total_profit

    def maxProfit2(self, prices: Lits[int]) -> int:
        """
        The problem involves finding the maximum profit that can be achieved by buying and selling stocks on different days. 
        The key observation is that we can achieve the maximum profit by summing up all the positive differences between consecutive days. 
        This effectively means buying on one day and selling on the next day whenever the price is higher on the next day.

        Someone's solution with much less code
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
