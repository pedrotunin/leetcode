from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = max(heights)

        minR = [len(heights)] * len(heights)
        minL = [-1] * len(heights)
        
        stack = []

        for i, h in enumerate(heights):
            while stack and h < stack[-1][0]:
                _, stackInd = stack.pop()
                minR[stackInd] = i
            stack.append([h, i])

        stack = []

        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            while stack and h < stack[-1][0]:
                _, stackInd = stack.pop()
                minL[stackInd] = i
            stack.append([h, i])
        
        for i, h in enumerate(heights):
            indMinR = minR[i]
            indMinL = minL[i]

            if i == indMinR and i == indMinL:
                res = max(res, h * len(heights))


            elif i == indMinR:
                res = max(res, 
                          heights[indMinL] * (i - indMinL + 1),
                          heights[i] * (i - indMinL)
                          )

            elif i == indMinL:
                res = max(res, 
                          heights[indMinR] * (indMinR - i + 1),
                          heights[i] * (indMinR - i)
                          )
            else:
                area = (indMinR - indMinL - 1) * heights[i]
                res = max(res, area)

        return res

print(Solution().largestRectangleArea([1,2,3,4,5]))