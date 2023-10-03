def serch(arr,target,strt,end):
    # sourcery skip: assign-if-exp, chain-compares, remove-unnecessary-else
    if strt>end:
        return -1 
    
    mid=(strt+end)//2
    if arr[mid] == target:
        return mid
    if arr[strt]<=arr[mid]: # target ele on l1 or l2
        if arr[strt]<=target and target<=arr[mid]:
            return serch(arr,target,strt,mid-1)
        else:
            return serch(arr,target,mid+1,end)
    else:
         if arr[mid] <= target and target <= arr[end]:
            return serch(arr,target,mid+1,end)
         else:
            return serch(arr,target,strt,mid-1)