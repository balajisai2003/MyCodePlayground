# def invert_bits(n): 
#     return "".join("1" if bit == "0" else "0" for bit in n) 

# def max_sum(lst, k): 
#     mxval = max(lst) 
#     mxindex = lst.index(mxval) 
#     left = max(0, mxindex-k) 
#     right = min(len(lst)-1, mxindex+k) 
     
#     selected = lst[left:mxindex+1] + lst[mxindex:right+1]  
#     lst = [x for x in lst if x not in selected] 
     
#     return sum(selected), lst 

# # Input  
# lst = list(map(int, input().split()))   
# a1, b1 = input().split() 
# a2, b2 = input().split() 
# k = int(input()) 

# sum1, sum2 = 0, 0 

# while lst: 
#     s1, lst = max_sum(lst, k)  
#     sum1 += s1 
     
#     if not lst: 
#         break 
         
#     s2, lst = max_sum(lst, k) 
#     sum2 += s2 
     
# if sum1 > sum2: 
#     a1 = invert_bits(a1) 
#     b2 = invert_bits(b2) 
# else: 
#     a2 = invert_bits(a2)  
#     b1 = invert_bits(b1) 

# xor1 = int(a1, 2) ^ int(b1, 2)   
# xor2 = int(a2, 2) ^ int(b2, 2) 

# if xor1 > xor2: 
#     print("Rahul",end="") 
# elif xor2 > xor1: 
#     print("Rupesh",end="") 
# else: 
#     print("both",end="")




# def toggle(num):
#     result = ""
#     for bit in num:
#         if bit == "0":
#             result += "1"
#         else:
#             result += "0"
#     return result

# def get_max_sum(arr, k):
#     max_val = max(arr)
#     max_index = arr.index(max_val)
#     left = max(0, max_index-k)
#     right = min(len(arr)-1, max_index+k)
    
#     selected = arr[left:max_index+1] + arr[max_index:right+1] 
#     arr = [x for x in arr if x not in selected]
    
#     return sum(selected), arr

# # Input 
# arr = list(map(int, input().split()))  
# a1, b1 = input().split()
# a2, b2 = input().split()
# k = int(input())

# sum1, sum2 = 0, 0

# while arr:
#     s1, arr = get_max_sum(arr, k) 
#     sum1 += s1
    
#     if not arr:
#         break
        
#     s2, arr = get_max_sum(arr, k)
#     sum2 += s2
    
# if sum1 > sum2:
#     a1 = toggle(a1)
#     b2 = toggle(b2)
# else:
#     a2 = toggle(a2) 
#     b1 = toggle(b1)

# xor1 = int(a1, 2) ^ int(b1, 2)  
# xor2 = int(a2, 2) ^ int(b2, 2)

# if xor1 > xor2:
#     print("Rahul")
# elif xor2 > xor1:
#     print("Rupesh")
# else:
#     print("both")



