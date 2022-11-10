import fileinput

def check(chr):
    if chr == '.' or chr == '?' or chr == '!':
        return True
    return False

for line in fileinput.input() :
    s = ''
    for word in line.split():
        for i in range(len(word)):
            if check(word[i]):
                print(s.strip().capitalize())
                s = ''
            else :
                s += word[i]
        s += ' '
                