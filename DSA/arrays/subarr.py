
l = [1,2,3,4,5,6,7,8,9,10]

def sarr(l):
     for i in range(len(l)):
         for j in range(i, len(l)):
             print(l[i:j+1])

sarr(l)