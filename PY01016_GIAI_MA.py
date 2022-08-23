
def decode(s):
    for i in range(0, len(s), 2):
        k = int(s[i + 1])
        for j in range(k):
            print(s[i], end = "")
    print()

def Test():
    numOfTest = int(input())
    for test in  range(numOfTest):
        s = str(input())
        decode(s)
Test()