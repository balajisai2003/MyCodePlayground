nums = [1,2,3,4]
l=[]
for i in range(1,len(nums),2):
    l.extend([nums[i]]*nums[i-1])
print(l)