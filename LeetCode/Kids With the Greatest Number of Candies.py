candies = [4,2,1,1,2]
extraCandies = 1
m=max(candies)
for i in range(len((candies))):
    if candies[i]+extraCandies>=m:
        candies[i]=True
    else:
        candies[i]=False
print(candies)