def frequencyCount( arr, P):
    dic = {i: 0 for i in range(1, P + 1)}
    for i in arr:
        dic[i]+=1
    return list(dic.values())
