s = "Let's take LeetCode contest"
l = s.split()
ans = ""
for i in l:
    ans += i[::-1]

ans=ans[:-1]