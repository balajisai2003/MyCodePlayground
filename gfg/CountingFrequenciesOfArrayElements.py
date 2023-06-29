def countFreq(arr):
    dict={}
    for i in arr:
        if i in dict.keys():
            dict[i]+=1
        else:
            dict[i]=1
    for key,values in dict.items():
        print(key , values)
        print(dict)
if __name__ == '__main__':
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    n = len(arr)
    countFreq(arr)