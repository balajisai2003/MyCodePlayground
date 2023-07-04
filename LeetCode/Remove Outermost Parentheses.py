class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n=0
        ans = ""
        for i in s:
            if n in [1, 0]:
                ans+=""
            if i == "(":
                if n != 0:
                    ans +="("
                n+=1
            else:
                if n != 1:
                    ans +=")"
                n-=1
                # print(ans)
        return ans

obj = Solution()
print(obj.removeOuterParentheses(s = "(()())(())"))