# n=int(input())
# binNum = 0
# i=1
# while n>0:
#     # print(i,n,binNum)
#     binNum += i*(n%2)
#     n//=2
#     i*=10
# print(binNum)



def binrec(n,i,binNum):
    if n==0:
        return binNum
    binNum+=i*(n%2)
    n//=2
    i*=10
    return binrec(n,i,binNum)
print(binrec(47,1,0))