def getGreatestLess(number):
    if len(number) == 1:
        return -1
    index = len(number)
    for i in range(len(number) - 2, 0, -1):
        if int(number[i]) > int(number[i + 1]):
            index = i
            break
    if index != len(number):
        lastIndex = index + 1
        for j in range(index + 1, len(number), 1):
            if int(number[j]) < int(number[index]) and int(number[j]) > int(number[lastIndex]):
                lastIndex = j
        newNumber = number[0:index] + number[lastIndex] + number[index+1:lastIndex] + number[index] + number[lastIndex+1::]
        if len(str(int(newNumber))) == len(number):
            return  newNumber
    return -1

test = int(input())
while test > 0:
    test -= 1
    print(getGreatestLess(str(input())))
