from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = 0
        for i, p in enumerate(prices):
            if i == 0:
                minPrice = p
            else:
                res = max(res, p - minPrice)
                minPrice = min(minPrice, p)

        return res
