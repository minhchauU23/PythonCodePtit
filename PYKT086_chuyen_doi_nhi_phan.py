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

f = open("DATA.in")
test = int(f.readline().strip())
while test > 0:
    test -= 1
    tp = int(f.readline().strip())
    nb = int(f.readline().strip(), 2)
    print(convert(nb, tp))