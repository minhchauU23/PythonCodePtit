def findSubString(super, sub):
    st = 0
    cnt = 0
    while True:
        index = str.find(super, sub, st)
        if index == -1: return cnt
        cnt += 1
        st = index + len(sub)


test = int(input())
while test > 0:
    test -=1
    num = str(input())
    substr = str(input())
    print(findSubString(num, substr))