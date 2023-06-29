def bubblesort(l):
    for turn in range(len(l)-1):
        for i in range(len(l)-1-turn):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
    print(l)
bubblesort([2,3,4,5,-61,2,3,7])

