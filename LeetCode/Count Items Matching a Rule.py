from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d={"type":0, "color":1, "name":2}
        indx = d[ruleKey]
# sourcery skip: simplify-constant-sum
        return sum(1 for i in items if i[indx] == ruleValue)
    

obj = Solution()
print(obj.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))