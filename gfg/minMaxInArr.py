def minMaxInArr(arr):
    min = arr[1]
    max = arr[1]
    for i in arr:
        if min > i:
            min = i
        if max < i:
            max = i
    return min,max
