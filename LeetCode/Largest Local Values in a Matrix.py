from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)-2
        resArr = [n*[0] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                resArr[i][j] = max([grid[a][b] for a in range(i,i+3) for b in range(j,j+3)])
        return resArr
obj  = Solution()
print(obj.largestLocal(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))