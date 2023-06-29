t=int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    dic={key:0 for key in arr }
    for i in arr:
        dic[i]+=1
    s=[]
    for key, val in dic.items():
        if val > k:
            s.append(key)
    print(*(s))