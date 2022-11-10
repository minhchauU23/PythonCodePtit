
def convert(num, type):
    res = ""
    if num == 0:
        return 0
    while num > 0:
        mod = num % type
        if(mod >= 10):
            res += chr(ord('A') + mod-10)
        else:
            res +=  str(num % type)
        num //=type
    return res[::-1]

test = int(input())
while test > 0:
    test -= 1
    num, type = input().split()    
    print(convert(int(num), int(type)))