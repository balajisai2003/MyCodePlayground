n=9
def conv(n,b):
    s=""
    while n:
        s=str(n%b)+s
        n=n//b
    return s
conv(n,2)
for i in range(2,n-1):
    s=conv(n,i)
    if s!=s[::-1]:
        print(i,False)
    else:
        print(i,True)
