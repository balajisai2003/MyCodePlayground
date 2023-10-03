def mergeSort(arr,start,end):
    if start >= end:
        return
    mid = (start+end)//2
    mergeSort(arr,start,mid) # left part
    mergeSort(arr,mid+1,end) # Right part
    merge(arr,start,mid,end)

def merge(arr,start,mid,end):
    temp = [None]*(end-start+1)
    i = start
    j = mid+1
    k=0 # iterator for temp arr
    while i<=mid and j <= end:
        if arr[i]<arr[j]:
            temp[k] = arr[i]
            i+=1
        else:
            temp[k] = arr[j]
            j+=1
        k+=1

    while i<=mid:
        temp[k] = arr[i]
        k+=1
        i+=1


    while j<=end:
        temp[k] = arr[j]
        k+=1
        j+=1

    for i in range(len(temp)):
        arr[start+i] = temp[i]


arr = ["fghj","dfg","lkl","jih","poi"]

mergeSort(arr,0,len(arr)-1)

print(arr)