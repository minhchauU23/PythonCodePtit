
def check(num):
    for index in range(len(num)):
        if(num[index] != '4' and num[index] != '7'): 
            return False
    return True


def Test():
    test = int(input())
    while test > 0:
        num = input()
        print("YES" if check(num) else "NO")
        test -= 1

Test()