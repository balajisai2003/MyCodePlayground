from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                k+=1
                nums[k-1] = nums[i]
        for i in range(k,n):
            nums[i] = "_"
        return k,nums
        # return k
obj = Solution()
print(obj.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))