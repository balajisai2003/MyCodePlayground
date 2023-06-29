class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {i: 0 for i in jewels}
        for i in stones:
            if i in d:
                d[i]+=1
        return sum(d[i] for i in jewels)

obj = Solution()
print(obj.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))


