import math

def distance(x1,y1,x2,y2):
  ans=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
  return math.ceil(ans)

def area(d):
    return math.ceil(3.14*d*d)

def perfect(n):
    x=math.floor(math.sqrt(n))
    if (math.sqrt(n)-math.floor(math.sqrt(n))==0):
        return n
    above=(x+1)*(x+1)
    below=x*x
    diff1=above - n
    diff2= n - below
    if (diff1 > diff2):
        return below
    else:
        return above

c1,c2=map(int,input().split())
r1,r2=map(int,input().split())
w1,w2=map(int,input().split())

actual=area(distance(c1,c2,r1,r2))
wrong=area(distance(c1,c2,w1,w2))

if(actual==wrong):
    print('-1',end="")
elif(actual>wrong):
    money=(actual-wrong)*20
    print("Krishna ",end="")
    print(money,end="")
else:
    diff=wrong-actual
    near=perfect(diff)
    if(near<diff):
        money=abs((diff-near)*20)
        print("Shiva ",end="")
        print(money,end="")
    else:
        money=abs((diff-near)*20)
        print("Krishna ",end="")
        print(money,end="")