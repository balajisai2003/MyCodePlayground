arr = [1,2,4,5,6]
# print(sum(arr)-len(arr)*((len(arr)+1)/2))

tv = 0

for i in arr:
    tv^=i
for i in range(1,7):
    tv^=i
print(tv)