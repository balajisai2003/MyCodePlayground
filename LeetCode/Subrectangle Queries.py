from typing import List

# class SubrectangleQueries:

#     def __init__(self, rectangle: List[List[int]]):
#         self.rectangle  = rectangle

        

#     def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
#         # sourcery skip: use-itertools-product
#         for i in range(row1,row2+1):
#             for j in range(col1,col2+1):
#                 self.rectangle[i][j] = newValue
        

#     def getValue(self, row: int, col: int) -> int:
#         return self.rectangle[row][col]
        
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle  = rectangle
        self.inp = []
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.inp.append((row1,col1,row2,col2,newValue))
        

    def getValue(self, row: int, col: int) -> int:
        return next(
            (
                newValue
                for row1, col1, row2, col2, newValue in reversed(self.inp)
                if row >= row1 and row <= row2 and col >= col1 and col <= col2
            ),
            self.rectangle[row][col],
        )


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)


obj = SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]])
