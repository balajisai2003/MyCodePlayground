# n=4
# for i in range(n):
#     for j in range(n):
#         if i == j or j==n-i-1 :
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print("")
# value = 64
# n=5
# for i in range(1,n+1):
#     for j in range(0,i):
#         value+=1
#         print(chr(value),end=" ")
#     print("")
        

# def recAlphaPat(n,value,i,string):
#     if i == n:
#         print(string)
#         return
        #   print(chr(value),end=" ")
#     recAlphaPat(value+1)


def recAlphaPat(n,value,i):
    if i==n: 
        return
    for j in range(i):
        print(chr(value+j),end=" ")
    print("")
    recAlphaPat(n,value+i,i+1)

recAlphaPat(5,65,0)
