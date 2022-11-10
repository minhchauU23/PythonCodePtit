from math import isqrt


prime = [True for i in range(0, 1000001)]

def erathone():
    prime[0] = False
    prime[1] = False
    for i in range(4, 1000001, 2):
        prime[i] = False
    for i in range(3, isqrt(1000001), 2):
        if prime[i] == True:
            for j in range(i*i, 1000001, i):
                prime[j] = False



erathone()
test = int(input())
while test > 0:
    test -= 1
    N = int(input())
    cnt = 0
    for i in range(3, N, 2):
        if i + 6 >= min(N, len(prime)): break
        if prime[i] and prime[i+6]:
            if prime[i+2]:
                cnt += 1
            if prime[i+4]:
                cnt += 1
    print(cnt)