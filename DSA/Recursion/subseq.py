def subseq(arr,i):
    if i==len(arr):
        return
    for j in range(i,len(arr)):
        print(arr[j],end=" ")
    print("")
    return subseq(arr,i+1)
subseq([1,2,3],0)
