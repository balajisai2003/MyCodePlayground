def staircaseSearch(mat,key):
    row = 0
    col = len(mat[0])-1
    while (row<len(mat) and col >=0):
        if key == mat[row][col]:
            print(row,col)
            break
        if key < mat[row][col]:
            col-=1
        if key>mat[row][col]:
            row+=1
    print("-------------*************---------------")
staircaseSearch([[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]],33)