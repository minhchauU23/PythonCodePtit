def convert(decimalNum, typeNum):
    newNum = ""
    while decimalNum > 0:
        mod = decimalNum % typeNum
        decimalNum//=typeNum
        if mod < 10: newNum += str(mod)
        else: newNum += chr(ord('A') + mod - 10)
    return newNum[::-1]



test = int(input())
while test > 0:
    test -= 1
    decimalNum, typeNum = input().split()
    print(convert(int(decimalNum), int(typeNum)))