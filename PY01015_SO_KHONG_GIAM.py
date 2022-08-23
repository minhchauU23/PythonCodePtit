def isAsendingNumber(s):
    for index in range(1, len(s)):
        if s[index] < s[index - 1]:
            return False
    return True


def Test():
    numOftest = int(input())
    for test in range(numOftest):
        s = str(input())
        print("YES" if isAsendingNumber(s) else "NO")

Test()