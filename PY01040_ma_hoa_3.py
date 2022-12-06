def devide(s):
    return (s[0:len(s)//2], s[len(s)//2::])

def totalStep(s):
    sum = 0
    for i in range(len(s)):
        sum += (ord(s[i]) - ord('A'))
    return sum

def rorate(s, step):
    newStr = ""
    for i in range(len(s)):
        newStr += chr(((ord(s[i]) - ord('A') + step)%26) + ord('A'))
    return newStr

def merge(left, right):
    newStr = ""
    for i in range(len(left)):
        newStr += rorate(left[i:i+1], ord(right[i]) - ord('A'))
    return newStr

def encode(s):
    dv = devide(s)
    leftRorate = rorate(dv[0], totalStep(dv[0]))
    rightRorate = rorate(dv[1], totalStep(dv[1]))
    return merge(leftRorate, rightRorate)

test = int(input())
while test > 0:
    test -= 1
    s = str(input())
    print(encode(s))