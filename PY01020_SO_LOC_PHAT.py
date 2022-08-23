def isLuckyNumber(s):
    if s[-2 :] == "86":
        return "YES"
    return "NO"

def Test():
    numOfTest = int(input())
    for test in range(numOfTest):
        s = str(input())
        print(isLuckyNumber(s))
Test()