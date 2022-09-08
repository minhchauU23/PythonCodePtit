
prime = []
nonPrime = [0, 1]

def erathone():
    for i in range(2, 501):
        if not i in nonPrime:
            prime.append(i)
            for j in range(i*i, 501, i):
                if not j in nonPrime:
                    nonPrime.append(j)


def check(num):
    for i in range(len(num)):
        if i in prime and  not int(num[i]) in prime:
            return False
        elif i in nonPrime and not int(num[i]) in nonPrime:
            return False
    return True

erathone()
test = int(input())
while test > 0:
    test-=1
    num = str(input())
    print("YES" if check(num) else "NO")