l = [1,2,3,4,5,6,7]
k=1
k %= 7
temp = [l[i] for i in range(k)]
for i in range(len(l)-k): 
    l[i] = l[i+k]
for i in range(len(l)-k,len(l)):
    l[i] = temp[i-(len(l)-k)]
print(l)