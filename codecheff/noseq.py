for i in range(int(input())):
    n,k,s=list(map(int,input().split()))
    t=s
    l=[]
    for i in range(1,n):
        p=k**i-1
        if p+m<=s:
            l.append((1,i-1))
        else:
            l.append((-1*p,i-1))
    