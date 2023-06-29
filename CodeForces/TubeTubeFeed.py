for _ in range(int(input())):
    n,t = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    maxEntertainment = -1
    ans =0
    for i in range(n):
        if i+a[i] <= t and b[i]>maxEntertainment:
            maxEntertainment = b[i]
            ans=i+1
    print( -1 if (maxEntertainment == -1) else ans)

