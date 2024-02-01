from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temperature, indice)
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):        
            while stack and t < stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res
    
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))