


# def mergesort(arr ,strt , end):
#     if strt>=end:
#         return
#     mid = (strt+end)//2

#     mergesort(arr,strt,mid)
#     mergesort(arr,mid+1,end)
#     merge(arr,strt,mid,end) # work

# def merge(arr,strt,mid,end):
#     temp = [0]*(end-strt+1)
#     i=strt
#     j = mid+1
#     k=0
#     while i<=mid and j<=end:
#         if arr[i]<arr[j]:
#             temp[k] = arr[i]
#             i+=1
#         else:
#             temp[k] = arr[j]
#             j+=1
#         k+=1

#     while i<= mid:
#         temp[k] = arr[i]
#         i+=1
#         k+=1
#     while j<= end:
#         temp[k] = arr[j]
#         j+=1
#         k+=1
#     for i in range(end-strt+1):
#         arr[strt+i] = temp[i]



# ##############################################################################

# def quickSort(arr,strt,end):
#     if strt>=end:
#          return
    
#     pivotindx = partition(arr,strt,end)
#     quickSort(arr,strt,pivotindx-1)
#     quickSort(arr,pivotindx+1,end)

# def partition(arr ,strt,end):
#     pivot = arr[end]
#     i = strt-1
#     for j in range(strt,end):
#         if arr[j]<pivot:
#             i+=1
#             arr[i],arr[j] = arr[j],arr[i]
#     i+=1
#     arr[end],arr[i] = arr[i],arr[end]

#     return i

# ####################################################
# arr = [2,3,1,7,6,5,8,4,5,46,3,4,2,1]

# # mergesort(arr,0,len(arr)-1)
# quickSort(arr,0,len(arr)-1)
# print(arr)

# def countDigits(n: int) -> int:
#     num = n
#     c=0 
#     while num > 0:
#         rem = num%10
#         if rem != 0 and  n%rem == 0:
#             c+=1
#         num//=10
#     return c
# print(countDigits(35))

# def permute(a, l, r,d):
    
#     if l == r:
#         if "".join(a) not in d:
#             d["".join(a)] = 1
#             print(''.join(a))
#     else:
#         for i in range(l, r):
#             a[l], a[i] = a[i], a[l]
#             permute(a, l+1, r,d)
#             a[l], a[i] = a[i], a[l] 


# n = int(input())
# m = int(input())
# a = "i"*m+"-"*(n-m)
# a=list(a)
# # permute(a,0,n,{})


# from datetime import datetime

# rahulinTime = datetime.strptime(input(),"%Y-%m-%d %H:%M:%S")
# rahuloutTime = datetime.strptime(input(),"%Y-%m-%d %H:%M:%S")
# rohitinTime = datetime.strptime(input(),"%Y-%m-%d %H:%M:%S")
# rohitoutTime = datetime.strptime(input(),"%Y-%m-%d %H:%M:%S")

# print(int((rahuloutTime-rahulinTime).total_seconds()+(rohitoutTime-rohitinTime).total_seconds()))



