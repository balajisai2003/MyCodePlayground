class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        sol = 0
        for i in s: 
            if i == "L":
                num-=1
            elif i == "R":
                num+=1
            if num == 0:
                sol+=1
        return sol
obj = Solution()
print(obj.balancedStringSplit("RLRRRLLRLL"))