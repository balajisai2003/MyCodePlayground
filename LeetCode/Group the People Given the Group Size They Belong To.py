from typing import List
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]] = [1,[i]]
            elif d[groupSizes[i]][0] == groupSizes[i]:
                d[groupSizes[i]][0] = 1
                d[groupSizes[i]].append([i])
            else:
                n = len(d[groupSizes[i]])
                d[groupSizes[i]][n-1].append(i)
                d[groupSizes[i]][0]+=1
        mykeys = sorted(d.keys())
        ans = []
        for i in mykeys:
            ans.extend(d[i][1:])
        return ans
o = Solution()
print(o.groupThePeople(groupSizes = [2,1,3,3,3,2]))