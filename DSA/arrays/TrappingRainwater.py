def trappedRainWater(l):
    # left max boundary array
    lmb = [l[0]]
    for i in range(1, len(l)):
        lmb.append(max(l[i],lmb[i-1]))
    #  right max bound array
    rmb = [l[-1]]
    for i,j  in enumerate(l[-2::-1]):
        rmb.append(max(j,rmb[i]))
    rmb=rmb[::-1]
    trappedWater = 0
    for i in range(len(l)):
        waterlevel = min(lmb[i],rmb[i])
        trappedWater+=(waterlevel-l[i])
    print(rmb,lmb,trappedWater)

l = [4,2,0,6,3,2,5]
trappedRainWater(l)
