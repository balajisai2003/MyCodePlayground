def selction(l):
    n=len(l)
    for i in range(n-1):
        minPos = i
        for j in range(i+1,n-1):
            if l[minPos]>l[j]:
                minPos = j
        l[minPos],l[i] = l[i],l[minPos]
    print(l)
selction([1,3,2,4,2,5,7,8])