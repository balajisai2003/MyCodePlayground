def insertionsort(l=None):
    if l is None:
        l = [2,1,4,5,-61,2,3,7]
    for i in range(1,len(l)):
        current = l[i]
        pos = i
        while current < l[pos-1] and pos>0:
            l[pos] = l[pos-1]
            pos -= 1
        l[pos] = current
    print(l)
    