
from pickle import TRUE


def check(str):
    if str[2] == '+':
        return (int(str[0]) + int(str[4])) == int(str[8])
    elif str[2] == '-':
        return int(str[0]) - int(str[4]) == int(str[8])
    elif str[2] == '*':
        return int(str[0]) * int(str[4]) == int(str[8])    
    else:
        return int(str[0]) / int(str[4]) == int(str[8])



str = input()
print("YES" if check(str) else "NO")

