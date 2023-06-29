import math
def pf(n):
    l=[]
    while n%2==0:
        l.append(2)
        n=n/2
    for i in range(3,int(math.sqrt(n))+1):
        while n%i==0:
            l.append(i)
            n=n/i
    if n>2:
        l.append(n)
pf(8)
