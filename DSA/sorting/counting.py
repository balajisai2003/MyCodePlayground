l = [2,1,4,5,2,3,7,7]


def countingSort(l):
    mx = max(l)
    # print(mx)
    size = [0]*(mx+1)
    # print(size,len(size))
    for i in l:
        size[i]+=1
    j=0
    for i in range(mx+1):
        while size[i]>0:
            l[j] = i
            j+=1
            size[i]-=1
    print(l)


countingSort(l)