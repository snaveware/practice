
import random
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range(len(nums)):
                if j==i:
                    continue
                if nums[i] + nums[j] == target:
                    return [i,j]

nums = [2,7,11,15]
target = 9
indices = Solution().twoSum(nums,target)

print("indices: ",indices)