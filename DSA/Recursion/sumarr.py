def sumArr(arr,i,s):
    if i==len(arr):
        return s
    s+=arr[i]
    return sumArr(arr,i+1,s)


print(sumArr([1,2,3,4,5,6],0,0))