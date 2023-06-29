class Solution:
    def minimumSum(self, num: int) -> int:
        l=[]
        while num>0:
            l.append(num%10)
            num //= 10
        l.sort()
        n=len(l)
        return sum(((l[i]*10)+l[n-1-i]) for i in range(n//2))
    
obj = Solution()
print(obj.minimumSum(num = 29390902))