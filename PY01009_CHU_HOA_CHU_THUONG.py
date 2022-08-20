


myString = str(input())

upperCase = 0
for index in range(len(myString)):
    if myString[index] >= 'A' and myString[index] <= 'Z':
        upperCase += 1


if upperCase <= len(myString)/2:
    print(myString.lower())
else:
    print(myString.upper())