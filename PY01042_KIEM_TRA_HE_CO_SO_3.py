
def isTenaryNumber(num):
    for i in range(len(num)):
        if num[i] != '0' and num[i] != '1' and num[i] != '2':
            return False
    return True
    

test = int(input())
while test > 0:
    test -= 1
    num = str(input())
    print("YES" if isTenaryNumber(num) else "NO")
