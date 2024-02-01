from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        asc = [0] * len(nums)
        desc = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                asc[i] = nums[i]
            else:
                asc[i] = asc[i-1] * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                desc[i] = nums[i]
            else:
                desc[i] = desc[i+1] * nums[i]

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(desc[i+1])
            elif i == len(nums) - 1:
                res.append(asc[i-1])
            else:
                res.append(asc[i-1] * desc[i+1])

        return res

Solution().productExceptSelf([1,2,3,4])