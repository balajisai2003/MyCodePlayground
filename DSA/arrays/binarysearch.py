l= [1,2,3,4,5,6,7,8,9,10]
key = 3
def BinarySearch(l, key):
    start = 0
    end = len(l)-1
    while start <= end:
        mid = (start + end)//2
        if l[mid] == key:
            return mid
        elif l[mid] < key:
            start = mid + 1

        else:
            end = mid - 1
    
    return -1

val = BinarySearch(l, key)
print(val)