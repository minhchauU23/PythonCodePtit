


from email.mime import base
import math


def minNum(s):
    st = -1
    res = 1000000
    for i in range(len(s)):
        if str.isdigit(s[i]) and st == -1:
            st = i
        if s[i].isalpha() and st != -1:
            res = min(res, int(s[st:i]))
            st = -1 
    if st != -1:
        res = min(res, int(s[st:]))
    return res

test = int(input())
while test > 0:
    test -=1
    s = str(input())
    print(minNum(s))