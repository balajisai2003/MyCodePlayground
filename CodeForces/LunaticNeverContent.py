from math import gcd,ceil

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(ceil(n/2)):
        ans = gcd(ans,abs(l[i]-l[n-i-1]))
    print(ans)
