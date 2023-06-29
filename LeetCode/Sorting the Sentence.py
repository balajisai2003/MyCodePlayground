class Solution:
    def sortSentence(self, s: str) -> str:
        d= {}
        l=s.split()
        for i in l:
            print(i)
            d[i[-1]] = i[:-1]
        print(d)
        ans = "".join(f"{d[str(i)]} " for i in range(1,len(l)+1))
        return ans[:-1]
obj = Solution()
print(obj.sortSentence(s = "is2 sentence4 This1 a3"))