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
    print(trappedWater)


def trap(height) :
        apex, ans = height.index(max(height)), 0
        for arr in [height[:apex], height[:apex:-1]]:
            limit = 0
            for val in arr:
                if val < limit:
                    ans += limit - val
                else:
                    limit = val
        return ans

l = [8,0,1,0,2,1,0,1,3]
print(trap(l[1:]))


