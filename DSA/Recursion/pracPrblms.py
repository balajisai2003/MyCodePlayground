# find indices of key val in given array of size N

def findKeys(arr,key,strt):
    if strt == len(arr) :
        return
    if arr[strt] == key:
        print(strt)
    return findKeys(arr,key,strt+1)

# findKeys([1,2,2,2,3,4,5],2,0)


# integer to words
digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]
def intTowrds(num):
    if num==0:
        return
    lastDigit = num%10
    intTowrds(num//10)
    print(digits[lastDigit] ,end=" ")
# intTowrds(123)

