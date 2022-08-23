def checkDistanChars(s):
    i, j = 0, len(s) - 1
    while i  < j:
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(s[j]) - ord(s[j -1])):
            return "NO"
        i += 1
        j -= 1
    return "YES"
def Test():
    numOfTest = int(input())
    for test in range(numOfTest):
        s = str(input())
        print(checkDistanChars(s))
Test()