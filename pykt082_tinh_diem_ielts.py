def getScore(correct):
    if correct >= 39: return 9.0
    if correct >= 37: return 8.5
    if correct >= 35: return 8.0
    if correct >= 33: return 7.5
    if correct >= 30: return 7.0
    if correct >= 27: return 6.5
    if correct >= 23: return 6.0
    if correct >= 20: return 5.5
    if correct >= 16: return 5.0
    if correct >= 13: return 4.5
    if correct >= 10: return 4.0
    if correct >= 7: return 3.5
    if correct >= 5: return 3.0
    if correct >= 3: return 2.5
    return 0

def roundScore(decimalPart):
    if decimalPart >= 0.75:
        return 1.0
    if decimalPart >= 0.25:
        return 0.5
    return 0


test = int(input())
while test > 0:
    test -= 1
    exam = input().split()
    natural = (getScore(int(exam[0])) + getScore(int(exam[1])) + float(exam[2]) + float(exam[3]))//4
    decimalPart = (getScore(int(exam[0])) + getScore(int(exam[1])) + float(exam[2]) + float(exam[3]))/4 - natural
    print(natural + roundScore(decimalPart))

