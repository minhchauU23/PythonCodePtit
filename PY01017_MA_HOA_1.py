from tokenize import String


def encode(s):
    res = ""
    post = 0
    for i in range(post + 1, len(s)):
        if s[i] != s[post]:
            res += str(i-post) + s[post]
            post = i
    res += str(len(s) - post) + s[post];
    return res

def Test():
    numOfTest = int(input())
    for test in range(numOfTest):
        s = str(input())
        print(encode(s))
Test()

print(str.upper())