from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float("inf")
        maximum = float("-inf")
        for i in prices:
            profit = i-minimum
            maximum = max(profit,maximum)
            minimum = min(minimum,i)
        return max(maximum, 0)