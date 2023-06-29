from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {indices[i]:s[i] for i in range(len(indices))}
        return "".join(d[i] for i in range(len(indices)))
obj = Solution()
print(obj.restoreString("codeleet",  [4,5,6,7,0,2,1,3]))