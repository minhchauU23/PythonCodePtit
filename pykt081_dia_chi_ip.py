test = int(input())
while test > 0:
    test -= 1
    ok = True
    ip = input().split(".")
    if len(ip) != 4:
        ok = False
    for i in ip:
        try:
            x = int(i)
            if x > 255 or x < 0:
                ok = False
                break
        except ValueError:
            ok = False
    print("YES" if ok else "NO")
