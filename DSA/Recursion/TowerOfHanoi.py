def TowerOfHanoi(n,fromRod,toRod,auxRod):
    if n == 1:
        print(F"disk 1 moved from {fromRod} to {toRod}")
        return
    TowerOfHanoi(n-1,fromRod,auxRod,toRod)
    print(f"disk {n} moved from {fromRod} to {toRod}")
    TowerOfHanoi(n-1,auxRod,toRod,fromRod)


TowerOfHanoi(3,"A","C","B")
