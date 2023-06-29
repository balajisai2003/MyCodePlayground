for _ in range(int(input())):
    n,x,k,p = list(map(int,input().split()))
    ans = 0
    if x>k :
        ans = (p+k*10)
    else:
        ans = ((x*10)+(k-x)*5+p)
    if k==n:
        ans +=20
    print(ans)
