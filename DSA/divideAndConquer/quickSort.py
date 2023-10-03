#  select pivot element (last element)
#  partition (parts)
#  recursively call quicksort
def partition(arr,strt,end):
    pivot = arr[end]
    i=strt - 1
    for j in range(strt,end):
        if arr[j]<= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i] # swap
    i+=1
    arr[end],arr[i] = arr[i],arr[end]

    return i

#  base case if strt >= end
#  work find pivot index
#  break it into left and right parts
def quickSort(arr,strt,end):
    if strt>=end:
        return
    pivotindx = partition(arr,strt,end)
    quickSort(arr,strt,pivotindx-1)
    quickSort(arr,pivotindx+1,end)

arr= [2,3,1,4,6,2,3,4,1,9,7,6,5,4,1]

quickSort(arr,0,len(arr)-1)

print(arr)
