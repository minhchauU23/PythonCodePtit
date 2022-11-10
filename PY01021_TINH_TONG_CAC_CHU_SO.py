
from tokenize import String


test = int(input())
while test > 0:
    test -= 1
    s = str(input())
    res = ""
    sum = 0
    for i in range(len(s)):
        if s[i].isdigit():
            sum += int(s[i])
        else:
            res += s[i]
    print(*sorted(res), sum, sep="")
