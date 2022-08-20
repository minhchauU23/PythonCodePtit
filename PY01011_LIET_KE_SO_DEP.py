
def isPalidrome(myString):
    for index in range(int(len(str(myString))/2)):
        if(myString[index] != myString[len(myString) - 1- index]): 
            return False
    return True

def Test():
    numOfTest = int(input())
    for test in range(numOfTest):
        sizeNum = int(input())
        queue = [2, 4, 6, 8]
        while True:
            top = queue.pop(0)
            if top > sizeNum : break
            if isPalidrome(top) :
                print(top)
            for num in range(0, 8, 2):
                queue.append(top*10+num)
            
Test()
        


