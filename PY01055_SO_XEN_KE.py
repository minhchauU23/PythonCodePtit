
def check(num):
    if len(num) %2 == 0 : return False
    if num[0] == num[1] : return False
    for i in range(2, len(num) -1, 2):
        if num[i] != num[0]: return False
    return True

test = int(input())
while test > 0:
    test -= 1
    num = str(input())
    print("YES" if check(num) else "NO")