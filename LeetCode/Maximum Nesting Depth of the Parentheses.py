s = "(1)+((2))+(((3)))"
mx=0
count=0
for i in range(len(s)):
    if s[i]=="(":
        count+=1
        mx=max(mx,count)
    if s[i]==")":
        count-=1
print(mx)
