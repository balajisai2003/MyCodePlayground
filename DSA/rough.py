# n = int(input("Enter the size of the array: "))
# alist = list(map(int, input(f"Enter {n} elements of the array: ").split()))
# d= {}
# for i in alist:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print("Duplicate elements:", end=" ")
# for i in d:
#     if d[i]>1:
#         print(i, end=" ")
# print()
# print("Unique elements:", end=" ")
# for i in d:
#     if d[i]==1:
#         print(i, end=" ")



# for _ in range(int(input())):
#     n,k = map(int,input().split())
#     arr = sorted(map(int,input().split()))
#     arr.reverse()
#     i = 0
#     res = 0
#     while k>0:
#         if arr[i] < arr[i + 1]:
#             i += 1
#         res+=arr[i]
#         arr[i] -= 1
#         k -= 1
#     print(res)
        

# # prime numbers between a, b
# def isPrime(n):
#     return False if n==1 else all(n%i != 0 for i in range(2, int(n**0.5)+1))
# for _ in range(int(input())):
#     a,b = map(int,input().split())
#     for i in range(a,b+1):
#         if isPrime(i):
#             print(i)
#     print()



# def isPrime(n):
#     return False if n==1 else all(n%i != 0 for i in range(2, int(n**0.5)+1))
# n = int(input())
# prime = next((i for i in range(n - 1, 1, -1) if isPrime(i)), 0)
# print(prime)



# s = input("Enter a string: ")
# d = {}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for i in sorted(d.keys()):
#     print(f"{i}: {d[i]}")

# def encryptedData(data, key):
#     data = str(data)
#     key = key%len(data)
#     print(key)
#     return int(data[key:]+data[:key])

# print(encryptedData("78512", 3))


# def sumOfDigits(n):
#     return n if n<10 else n%10 + sumOfDigits(n//10)

# def prodDelivery(orderID):
#     return [sumOfDigits(i) for i in orderID]

# print(prodDelivery([123, 456, 789, 12345]))

for i in range(int(input())):
    s = input()
    chars = ""
    nums = ""
    for i in s:
        if i.isalpha():
            chars+=i
        else:
            nums+=i
    print(chars+nums)