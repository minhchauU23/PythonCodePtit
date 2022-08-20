
def check(myString):
    str1 = myString[0:2]
    str2 = myString[len(myString)-2 :len(myString)]
    if(str1 == str2 ):
        return True
    return False

def Test():
    numOftest = int(input())
    for test in range(numOftest):
        myString = str(input())
        print("YES" if check(myString) == True else "NO")
Test()


