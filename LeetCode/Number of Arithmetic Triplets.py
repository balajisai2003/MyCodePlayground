nums = [0,1,4,6,7,10]
diff = 3
c=0
for i in nums:
    if i+3 in nums:
        if i+6 in nums:
            c+=1
print(c)