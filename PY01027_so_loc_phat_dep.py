from operator import truediv


def isGreatNumber(num):
    for index in range(len(num)):
        if num[index] == "8":
            if index == 0: return False
            elif index == 1:
                if num[index - 1] == "8": return False
            else:
                if num[index - 1] == "8" and num[index - 2] == "8":
                    return False
        elif num[index] != "6": return False
    return True


num = str(input())
print("YES" if isGreatNumber(num) else "NO")