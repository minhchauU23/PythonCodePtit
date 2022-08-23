
from unicodedata import decimal


def decode(k, s):
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    k = int(k)
    s = str(s)
    result = ""
    for i in range(-1,-len(s) - 1, -1):
        result += P[(P.find(s[i]) + k)%28] 
    return result

while True:
    ls = [str(i) for i in input().split()]
    if len(ls) == 1:
        break
    print(decode(ls[0], ls[1]))