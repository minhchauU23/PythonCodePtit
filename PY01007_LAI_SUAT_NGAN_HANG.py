
def calc(X, N, M):
    result = 0
    while pow(1 + X/100, result)*N < M:   
        result+=1
    return result

def Test():
    numOfTests = int(input())
    for test in range(numOfTests):
        N, X, M = map(float, input().split())
        print(calc(X, N, M))
Test()