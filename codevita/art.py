from sys import maxsize


def help(string):
    n = len(string)
    st = {string[0]}
    for i in range(1, n):
        if string[i] == string[i - 1]:
            continue
        if string[i] in st:
            return False
        st.add(string[i])
    return True


def minSwaps(string, l, r, cnt, minm):
    if l == r:
        return cnt if help(string) else maxsize
    for i in range(l + 1, r + 1, 1):
        string[i], string[l] = string[l], string[i]
        cnt += 1
        x = minSwaps(string, l + 1, r, cnt, minm)
        string[i], string[l] = string[l], string[i]
        cnt -= 1
        y = minSwaps(string, l + 1, r, cnt, minm)
        minm = min(minm, min(x, y))
    return minm


n = int(input())
alist = list(input().split())
ans = minSwaps(alist, 0, n - 1, 0, maxsize)
print(ans)
