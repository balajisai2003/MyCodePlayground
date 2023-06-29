N = 6
H = [9, 1, 2, 3, 1, 5]
l=[]
for i in range(1,N):
    if l and H[i-1]>=H[i]:
        l.pop()
    else:
        l.append(i)
print(N-len(l))