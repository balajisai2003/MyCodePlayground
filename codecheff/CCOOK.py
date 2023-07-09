d = {
    0:"Beginner",
    1:"Junior Developer",
    2:"Middle Developer",
    3:"Senior Developer",
    4:"Hacker",
    5:"Jeff Dean",
}

for _ in range(int(input())):
    l = list(map(int,input().split()))
    n = sum(l)
    print(d[n])