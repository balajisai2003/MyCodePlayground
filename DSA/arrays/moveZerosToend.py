l= [1,0,4,0,3,4,5,6,0,5,0]
j=0
for indx in range(len(l)):
    if l[indx] == 0:
        j = indx
        break
i = j+1

while(i<len(l)):
    if l[i] !=0:
        l[j],l[i] = l[i],l[j]

        j+=1
    i+=1
print(l)
