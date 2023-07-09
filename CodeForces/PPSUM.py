def sumOfn(n):
    return (n*(n+1))//2
for _ in range(int(input())):
    d, n = map(int, input().split())
    ans = (n*(n+1))//2
    for i in range(d-1):
        ans = (ans*(ans+1))//2
    print(ans)