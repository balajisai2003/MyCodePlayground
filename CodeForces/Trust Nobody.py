for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = -1
    for cheaters in range(n):
        cheating = sum(cheaters < l[j] for j in range(n))
        if cheaters == cheating :
            ans = cheaters
    print(ans)
