l = [7,1,5,3,6,4]

def buySEllstopck(l):
    mn = float("inf")
    mx = float("-inf")
    for i in l :
        profit = i-mn
        mx = max(profit,mx)
        mn = min(mn,i)
    print(mx)

buySEllstopck(l)