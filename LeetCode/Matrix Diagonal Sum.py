from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        mid = n//2
        m = n-1
        ans = sum((mat[i][i]+mat[i][m-i]) for i in range(n))
        if n%2!=0:
            ans-=mat[mid][mid]
        return ans
obj = Solution()
print(obj.diagonalSum(mat= [[1,2,3],
              [4,5,6],
              [7,8,9]]))

