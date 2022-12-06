from collections import deque

test = int(input())
while test > 0:
    test -= 1
    s = input()
    stk = deque()
    cnt = 0
    res = []
    for i in range(len(s)):
        if s[i] == "(":
            cnt += 1
            stk.append(cnt)
            res.append(cnt)
        elif s[i] == ")":
            res.append(stk.pop())
    print(*res)
