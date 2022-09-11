def isBanlancedString(myString):
    sz = len(myString)
    for i in range(0, sz//2):
        if abs(ord(myString[i]) - ord(myString[i + 1]) ) != abs(ord(myString[sz-i-1]) - ord(myString[sz-i-2]) ):
            return False
    return True


test = int(input())
while test > 0:
    test -= 1
    myString = str(input())
    print("YES" if isBanlancedString(myString) else "NO")