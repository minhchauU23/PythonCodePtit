
def doubNum(num):
    newNum = num
    while num > 0:
        newNum = newNum * 10 + num%10
        num //=10
    return newNum

def generate(listPalindrome):
    queue = [2, 4, 6, 8]
    while len(queue) > 0:
        top = queue[0]
        queue.pop(0)
        listPalindrome.append(int(doubNum(top)))
        for id in range(0, 9, 2):
            num = top * 10 + id
            if num >= 10000: break
            else :queue.append(num) 

def Test():
    listPalindrome = []
    generate(listPalindrome)
    numOfTest = int(input())
    for test in range(numOfTest):
        sizeNum = int(input())
        for item in listPalindrome:
            if item < sizeNum:
                print(item, end = ' ')
            else:
                print()
                break

Test()

        



