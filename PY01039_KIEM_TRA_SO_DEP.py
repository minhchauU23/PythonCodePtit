
def isGreatNumber(num):
    for i in range(1, len(num), 2):
        if i == len(num)-1:
            if num[i] == num[i-1] or num[i] != num[i-2]: return False
        else:
            if num[i] == num[i-1] or num[i-1] != num[i+1]:
                return False
    return True

test = int(input())
while test > 0:
    test-=1
    num = str(input())
    print("YES" if isGreatNumber(num) else "NO")