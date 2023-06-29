l = [1,2,3,4,5,6,7,8,9,10]
def prfxsubarrsum(l):  # sourcery skip: min-max-identity
    n = 0
    prfxarr = []
    for i in range(len(l)):
        n+=l[i]
        prfxarr.append(n)
    mx = float('-inf')
    print(prfxarr)
    for i in range(len(l)):
        for j in range(i, len(l)):
            currsum =   prfxarr[j] if i==0 else prfxarr[j]-prfxarr[i-1]
            if mx<currsum:
                mx = currsum
    return mx 

print(prfxsubarrsum(l))