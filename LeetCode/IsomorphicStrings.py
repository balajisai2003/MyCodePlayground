s = "egg"
t = "add"
def stts(s):
    dc={
    }
    n=1
    l=[]
    for i in s:
        if i in dc.keys():
            l.append(dc[i])
        else:

            dc[i]=n
            n += 1
            l.append(dc[i])
    return l
p= True if stts(s)==stts(t) else False
print(p)