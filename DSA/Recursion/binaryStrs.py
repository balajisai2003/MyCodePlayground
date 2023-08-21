def binaryStrs(n,lastEle,str):  # sourcery skip: use-fstring-for-concatenation
    if n==0:
        print(str)
        return 

    binaryStrs(n-1,0,str+"0")
    if lastEle == 0:
        binaryStrs(n-1,1,str+"1")
binaryStrs(3,0,"")