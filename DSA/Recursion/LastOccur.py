def lastOccur(arr,n,i):
    if arr[len(arr)-1-i] == n:
        return len(arr)-1-i
    if i == len(arr)-1:
        return -1
    return lastOccur(arr,n,i+1)


print(lastOccur([1,2,3,1,4,5,6,7],1,0))