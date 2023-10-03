l = [1,2,3,3,4,4,5,5]

i=0

for j in range(1,len(l)):
    if l[i]!=l[j]:
        i+=1
        l[i] = l[j]
print(l[:i+1])