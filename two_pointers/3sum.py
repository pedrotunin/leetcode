from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        sortedNums = sorted(nums)

        res = []
        h = {}
        
        for i, xi in enumerate(sortedNums):
            if i > 0 and xi == sortedNums[i - 1]:
                continue

            l = i + 1
            r = len(sortedNums) - 1

            while l < r:
                total = xi + sortedNums[l] + sortedNums[r]
                if total == 0:
                    resl = [xi, sortedNums[l], sortedNums[r]]
                    t = tuple(resl)
                    if t not in h:
                        res.append(resl)
                        h[t] = True
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res
    
print(Solution().threeSum([-1,0,1,2,-1,-4]))