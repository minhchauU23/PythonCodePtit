
def convert(num, type):
    step = 1
    if type == 4:
        step = 2
    if type == 8:
        step = 3
    if type == 16:
        step = 4
    num = "".join(reversed(num))
    res = ""
    for id in range(0, len(num), step):
        k = int(num[id:id + step][::-1], 2)
        if k >= 10 : res += chr(ord('A') + k -10)
        else : res = res + str(k)
    return res[::-1]


test = int(input())

while test > 0:
    test -=1
    type = int(input())
    num = str(input())
    
    print(convert(num, type))