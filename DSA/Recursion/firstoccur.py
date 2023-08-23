from typing import List

def frstOccur(arr : List[int],i: int,n: int):
    if arr[i]==n:
        return i
    if i==len(arr)-1:
        return -1
    
    return frstOccur(arr,i+1,n)

a=frstOccur([1,2,3,4,5,6,7],0,8)
print(a)

