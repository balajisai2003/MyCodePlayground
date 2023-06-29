l = [1,2,3,4,5,6,7,8,9,10]
print(sum(l))
def maxsubarr(l):
    mx = float('-inf')
    for i in range(len(l)):
        for j in range(i, len(l)):
            mx = max(mx, sum(l[i:j+1]))
    print(mx)
maxsubarr(l)