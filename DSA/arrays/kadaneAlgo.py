l = [1,2,3,4,-5,-6,-7,-8,-9,10]
def kadans(l):  # sourcery skip: min-max-identity
    mx = float('-inf')
    cs = 0 # cumulative sum
    for i in range(len(l)):
        cs += l[i]
        if cs<0:
            cs =0
        mx = max(cs,mx)
    print(mx)
kadans(l)