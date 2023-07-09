def oddOReve(n :int):
    bitmask : int = 1
    if (n and  bitmask) == 0:
        print("eve")
    else:
        print("odd")

oddOReve(9)