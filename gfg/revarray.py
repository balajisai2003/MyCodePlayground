t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s,end=0,n-1
    while s < end:
        arr[s], arr[end] = arr[end], arr[s]
        s += 1
        end -= 1
    sum = 0
    for indx, i in enumerate(arr):
        if indx % 2 == 0:
            sum += i ** 2
        else:
            sum -= i ** 2
    print(sum)
