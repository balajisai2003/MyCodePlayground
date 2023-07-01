from typing import List
class Solution:
    def digSum(self, num):
        sNum = 0
        while num > 0:
            sNum += num%10
            num//=10
        return sNum
    def differenceOfSum(self, nums: List[int]) -> int:
        sArr = sum(nums)
        for num in nums:
            sArr -= self.digSum(num)
        return abs(sArr)

obj = Solution()
print(obj.differenceOfSum(nums = [1,2,3,4]))