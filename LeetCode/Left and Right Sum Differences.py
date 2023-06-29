class Solution:
    def leftRightDifference(self, nums) :
        s =  sum(nums)
        lsum = 0
        rsum = s-nums[0]
        ans = []
        for i in range(1,len(nums)+1):
            ans.append(abs(lsum-rsum))
            if i==len(nums):
                break
            lsum+=nums[i-1]
            rsum-=nums[i]
        return ans
obj = Solution()
print(obj.leftRightDifference([10,4,8,3]))