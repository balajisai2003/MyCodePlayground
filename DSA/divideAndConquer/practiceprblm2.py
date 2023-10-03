# return max count number occur in array


def mjorEleInArr(arr,low,high):
    if low==high:
        return arr[low]
    mid = (low+high)//2
    left = mjorEleInArr(arr,low,mid)
    right = mjorEleInArr(arr,mid+1,high)

    if left == right:
        return left
    leftCount = CountInRange(arr,left,low,high)
    rightCount = CountInRange(arr,right,low,high)

    return left if leftCount>rightCount else right

def CountInRange(arr,ele,low,high):
    count = 0
    for i in range(low,high+1):
        if arr[i] == ele:
            count+=1
    return count

print(mjorEleInArr([1,23,3,3,3,4,4,4,5,5,5],0,len([1,23,3,3,3,4,4,4,5,5,5])-1))


for i in range(10):
    print(i)