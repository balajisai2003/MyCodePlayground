l = [-1,7 ,-3,4,5,6]

largest = l[0]
secondLargest = float("-inf")
smallest = l[0]
secondSmallest = float("inf")
for i in range(1,len(l)):
    if l[i]>largest:
        secondLargest = largest
        largest = l[i]
    if l[i]<largest and l[i]>secondLargest:
        secondLargest = l[i]

for i in range(1,len(l)):
    if l[i]<smallest:
        secondSmallest = smallest
        smallest = l[i]
    if l[i]>smallest and l[i]<secondSmallest:
        secondSmallest = l[i]

print(secondLargest,secondSmallest,smallest)