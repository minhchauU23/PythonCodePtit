from collections import OrderedDict
f = open("VANBAN.in","r")

wordDict = OrderedDict()
maxVal = 0
while True:
    line = f.readline().split()
    if len(line) == 0:
        break
    for word in line:
        if word == word[::-1]:
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict.update({word : 1})
            maxVal = max(maxVal, len(word))
f.close()
for word in wordDict:
    if len(word) == maxVal:
        print(word, wordDict[word], sep= " ")