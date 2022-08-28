
test = int(input())

while test > 0:
    test -=1
    s = str(input())
    print("YES" if s[0] == s[-1] else "NO")