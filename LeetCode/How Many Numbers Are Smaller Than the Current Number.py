nums = [8,1,2,2,3]
dic={}
for indx,i in enumerate(sorted(nums)):
    if i in dic:
        pass
    else:
        dic[i]=indx
l=[]
for i in nums:
    l.append(dic[i])
print(l)