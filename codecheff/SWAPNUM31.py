for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l = list(map(int,input().split()))
    m=n-k
    # r=k
    if m-1 >=k:
        l.sort()
    else:
        a = l[:m]+l[k:]
        a.sort()
        j=0
        for i in range(m):
            l[i] = a[j]
            j+=1
        for i in range(k,n):
            l[i] = a[j]
            j+=1
    print(*l)
    
    
    