def incOrder(n):
    if n==1:
        print(1 ,end=" ")
        return
    else:
        incOrder(n-1)
        print(n,end=" ")
incOrder(10)