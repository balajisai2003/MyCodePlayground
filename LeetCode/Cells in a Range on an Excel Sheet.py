from typing import List
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        # sourcery skip: inline-immediately-returned-variable, list-comprehension, use-itertools-product
        l=[]
        for i in range(ord(s[0]),ord(s[3])+1):
            l.extend(chr(i)+str(j) for j in range(int(s[1]),int(s[-1])+1))
        return l
obj = Solution()
print(obj.cellsInRange(s = "K1:L2"))