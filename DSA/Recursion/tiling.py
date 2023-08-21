def tiling(n):
    if n==1 or n==0:
        return 1
    vertical = tiling(n-1)
    horizontal = tiling(n-2)

    return vertical+horizontal
print(tiling(24151))