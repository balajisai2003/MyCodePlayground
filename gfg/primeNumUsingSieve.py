l=[1, 3, 5]
ll=[]
for i in range(1,100):
    if (6*i-1)%5==0:
        l.append((6*i+1))
        pass
    elif (6*i+1)%5==0:
        l.append((6 * i - 1))
        pass
    else:
        l.append(6*i-1)
        l.append(6 * i + 1)
print(l)
a, b, i, j = 0, 600, 0, 0
if (a == 1):
    print(a, end=" ")
    a += 1
    if (b >= 2):
        print(a, end=" ")
        a += 1
if (a == 2):
    print(a, end=" ")

    # MAKING SURE THAT a IS ODD BEFORE WE BEGIN
    # THE LOOP
if (a % 2 == 0):
    a += 1
    # NOTE : WE TRAVERSE THROUGH ODD NUMBERS ONLY
for i in range(a, b + 1, 2):

    # flag variable to tell
    # if i is prime or not
    flag = 1
    # WE TRAVERSE TILL SQUARE ROOT OF j only.
    # (LARGEST POSSIBLE VALUE OF A PRIME FACTOR)
    j = 2
    while (j * j <= i):
        if (i % j == 0):
            flag = 0
            break
        j += 1

    # flag = 1 means i is prime
    # and flag = 0 means i is not prime
    if (flag == 1):
        ll.append(i)

print(ll)