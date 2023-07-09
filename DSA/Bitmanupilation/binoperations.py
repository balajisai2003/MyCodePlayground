print(5 & 4) # AND operation
print(5 | 4) # OR operation
print(5 ^ 6) #XOR operation
print(~5) # ONE's complement operation
print(5<<2) # LEFT SHIFT opertion a<<b = a*2^b
print(5>>2) # RIGHT SHIFT opertion a>>b = a/2^b


def get_ith_bit (num,i):
    bitmask = 1<<i
    if num & bitmask == 0:
        print(0)
    else:
        print(1)

get_ith_bit(5,2)

def set_ith_bit(num ,i):
    bitmask = 1<<i
    print(num | bitmask)

set_ith_bit(10,2)

def clear_ith_bit(num, i):
    bitmask = ~(1<<i)
    print(num & bitmask)
    return num & bitmask

clear_ith_bit (10,2)

def update_ith_bit(num,i,newbit):
    # if newbit == 0:
    #     print(clear_ith_bit(num,i))
    # else:
    #     set_ith_bit(num,i)
    num = clear_ith_bit(num,i)
    bitmask = newbit<<i
    print(num | bitmask)    

print(update_ith_bit(10,2,1))