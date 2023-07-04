# Two sum using two pionter
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={key: value for value, key in enumerate(nums)}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in my_dict.keys() :
                if my_dict[c]!=i :
                    return [i,my_dict[c]]



obj = Solution()
print(obj.twoSum(nums = [2,7,11,15], target = 9))