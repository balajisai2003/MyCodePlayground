def xPowN(x,n):
    if n ==0:
        return 1
    return x*xPowN(x,n-1)
print(xPowN(2,3))


def XpowN(x,n):
    if n ==0:
        return 1
    if n%2==0:
        return XpowN(x,n//2)*XpowN(x,n//2)
    return x*XpowN(x,n//2)*XpowN(x,n//2)
print(XpowN(2,3))