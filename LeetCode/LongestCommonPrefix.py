l=["flower","flow","flight"]
l.sort()
print(l)
mn=len(l[0])
ans=''
for i in l:
    if len(i)<mn:
        mn=len(i)
for i in range(mn):
    if l[0][i] == l[-1][i]:
        ans+=l[0][i]
    else:
        break
print(ans)