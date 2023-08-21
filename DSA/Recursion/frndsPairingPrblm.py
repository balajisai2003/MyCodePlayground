def frndsPairingPrblm(n):
    if n==1 or n==2 :
        return n
    return frndsPairingPrblm(n-1)+(n-1)*frndsPairingPrblm(n-2)

print(frndsPairingPrblm(40))