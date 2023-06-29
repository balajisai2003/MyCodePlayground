 # lunatic
from math import gcd,ceil

for _ in range(int(input())):
    n = int(input())
    s = input()
    l= [ord(i) for i in s]

    print(l)
    ans = 0
    for i in range(ceil(n/2)):
        ans = gcd(ans,abs(l[i]-l[n-i-1]))
    print(ans)
    for i in l:
        print(i%ans)

# 4
# 2
# hi
# 8
# mallareddy
# 1
# b
# 3
# cpp


# s = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-orless normal distribution of letters, as opposed to using Content here content here making it look like readable English Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text and a search for lorem ipsum will uncover many web sites still in their infancy Various versions have evolved over the years sometimes by accident sometimes on purpose"
#
#
# l = list(s.split())
# print(len(l)-25)
# for i in l:
#     print(len(i))
#     print(i)

