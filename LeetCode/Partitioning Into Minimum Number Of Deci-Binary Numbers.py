s="9876534567890"
print(max(s))
m=0
for i in s:
    if m<int(i):
        m=int(i)
print(m)