def issorted(arr,i):
    if i==len(arr)-1:
        return True
    if arr[i]>arr[i+1]:
        return False
    return issorted(arr,i+1)
print(issorted([1,2,3,4,5,6,7,8,9],0))