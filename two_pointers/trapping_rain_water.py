from typing import List

class Solution:
    def trap(self, height: List[int]) -> int: # O(1) memory usage
        res = 0
        l, r = 0, len(height) - 1

        maxL = height[l]
        maxR = height[r]

        while l < r:
            if maxL <= maxR: # update left
                l += 1
                water = maxL - height[l]
                res += max(water, 0)
                maxL = max(maxL, height[l])

            else: # update right
                r -= 1
                water = maxR - height[r]
                res += max(water, 0)
                maxR = max(maxR, height[r])

        return res

    def trapUsingMemory(self, height: List[int]) -> int: # O(n) memory usage
        res = 0
        
        if len(height) < 3:
            return res

        maxL = [0] * len(height)
        maxR = [0] * len(height)

        for i, h in enumerate(height):
            if i == 0:
                maxL[i] = 0
            else:
                maxL[i] = max(maxL[i-1], height[i-1])
    
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                maxR[i] = 0
            else:
                maxR[i] = max(maxR[i+1], height[i+1])

        for i, h in enumerate(height):
            water = min(maxL[i], maxR[i]) - h

            if water > 0:
                res += water

        return res

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
