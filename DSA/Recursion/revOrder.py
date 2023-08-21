def reverseOrder(n):
    print(n,end=" ") #work
    if n ==1: #base case
        return
    else :
        reverseOrder(n-1) #call inner function
reverseOrder(10)