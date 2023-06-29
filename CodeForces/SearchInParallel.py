for _ in range(int(input())):
    n, x, y = list(map(int, input().split()))
    a,b = [], []
    freq = list(map(int, input().split()))
    v = [(val, i) for i, val in enumerate(freq, start=1)]
    v.sort(reverse=True)
    p1 = x
    p2 = y
    
    for i in range(n):
        if p1 <= p2:
            a.append(v[i][1])
            p1 += x
        else:
            b.append(v[i][1])
            p2 += y
        # print(a, b)
    print(a)
    print(b)



