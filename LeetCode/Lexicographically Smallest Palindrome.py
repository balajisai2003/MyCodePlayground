class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)//2):
            s[i] = s[len(s)-i-1]= min(s[i],s[len(s)-i-1])
        return "".join(s)
obj = Solution()
print(obj.makeSmallestPalindrome(s = "abcd"))