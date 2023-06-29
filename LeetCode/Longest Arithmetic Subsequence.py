from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        d= {}
        for i in range(n-1):
            for j in range(i+1,n):
                # print(nums[j]-nums[i])
                if nums[j]-nums[i] not in d:
                    d[nums[j]-nums[i]] = {nums[i],nums[j]}
                d[nums[j]-nums[i]] = d[nums[j]-nums[i]].union({nums[i],nums[j]})
        mx = float("-inf")
        ans  = None
        for i in d:
            if len(d[i])>mx:
                mx = len(d[i])
                ans = i
        return(list(map(int, d[ans])))
obj = Solution()
print(obj.longestArithSeqLength([3,6,9,12]))