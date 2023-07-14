from typing import List

            
class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        n = 0

        for i in range(len(nums)):

            if nums[i] != val:

                nums[n] = nums[i]

                n += 1
        print(n,nums)
obj = Solution()
obj.removeElement(nums = [3,2,2,3], val = 3)