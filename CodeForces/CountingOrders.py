for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    # mod = 1e9+7
    result = []
    ans =1
    a.sort()
    b.sort()
    j = 0
    for i in range(n):
        while a[j] <= b[i]:
            j+=1
        if j!=n:
            result.append(n-j)
    result.sort()
    for i in range(n):
        ans = ans * (result[i]-i)
    print(ans)