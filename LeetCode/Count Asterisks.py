class Solution:
    def countAsterisks(self, s: str) -> int:
        verticalBarount = 0
        AsterisksCount = 0
        for i in range(len(s)):
            if s[i] == "|":
                verticalBarount += 1 
            if verticalBarount % 2 == 0 and s[i] == "*":
                AsterisksCount += 1 
        return AsterisksCount