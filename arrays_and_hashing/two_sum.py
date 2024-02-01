from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums = list(zip(nums, range(len(nums))))
        nums: List[tuple] = sorted(nums)

        i = 0
        j = len(nums) - 1

        while(i != j):
            soma = nums[i][0] + nums[j][0]

            if soma == target:
                return [nums[i][1], nums[j][1]]
            elif soma < target:
                i += 1
            else:
                j -= 1

print(Solution().twoSum([3,2,4], 6))