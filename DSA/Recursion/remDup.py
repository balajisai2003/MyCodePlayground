def remdup(s,indx,newstr,maparr):
    if indx == len(s):
        return newstr
    if maparr[ord(s[indx])-ord("a")] == False:
        newstr+=s[indx]
        maparr[ord(s[indx])-ord("a")] = True
    return remdup(s,indx+1,newstr,maparr)
    
print(remdup("balaji",0,"",[False]*26))

    