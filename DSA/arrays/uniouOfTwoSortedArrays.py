l1 = [1,2,3,4,5,6,7,8,10]
l2 = [4,5,6,7,8,9]
rl = [l1[0]]
i=1
j=0
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j] and l1[i]>rl[-1]:
        rl.append(l1[i])
        i+=1
    elif l1[i]>l2[j] and l2[j]>rl[-1] :
        rl.append(l2[j])
        j+=1
    elif l1[i]==l2[j] and l1[i]>rl[-1]:
        rl.append(l1[i])
        j+=1
        i+=1
rl.extend(l1[i:]+l2[j:])
print(rl)