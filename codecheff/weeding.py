for _ in range(int(input())):
    n,m,k = list(map(int,input().split()))
    l= list(map(int,input().split()))
    if (l[-1]+k-1)<=m:
        print("yes")
    else:
        print("no")