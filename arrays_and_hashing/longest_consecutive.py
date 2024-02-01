from typing import List
import collections

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for num in nums:
            if num - 1 in s:
                continue
            
            count = 1
            while (num + count) in s:
                count += 1

            res = max(res, count)

        return res


print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))