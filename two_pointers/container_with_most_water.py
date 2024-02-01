from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        def area(i: int, j: int, hi: int, hj: int) -> int:
            return (j - i) * min(hi, hj)

        while l < r:
            actualL = l
            actualR = r
            actualArea = area(l, r, height[l], height[r])
            res = max(res, actualArea)

            if height[l] <= height[r]:
                l += 1
                while height[l] <= height[actualL] and l < r:
                    l += 1
            else:
                r -= 1
                while height[r] <= height[actualR] and r > l:
                    r -= 1

        return res