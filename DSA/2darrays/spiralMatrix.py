def printSpiral(l):
    sRow = 0
    sCol = 0
    endRow = len(l)-1
    endcol = len(l[0])-1

    while sRow<=endRow and sCol<=endcol:
        # top boundary
        for i in range(sCol ,endcol+1):
            print(l[sRow][i],"t")
        # right boundary
        for i in range(sRow+1,endRow+1):
            print(l[i][endcol],"r")
            
        #  bottom boundary
        for i in range(endcol-1,sCol-1,-1):
            print(l[endRow][i],"b")
        # left boudary
        for i in range(endRow-1,sRow,-1):
            print(l[i][sCol],"l")
        sRow+=1
        sCol+=1
        endRow-=1
        endcol-=1
printSpiral([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
