def sumIf(x1, x2, p, q):
    #p -> q
    len1, len2 = len(x1), len(x2)
    i = j = 0
    carry = 0
    res = ""
    while i < len1 and j < len2:
        k = int(x1[i]) + int(x2[j]) + carry
        if int(x1[i]) == p:
            k += q - p
        if int(x2[j]) == p:
            k += q - p
        res = res + str(k%10)
        carry = k//10
        i += 1
        j += 1
    while i < len1:
        k = int(x1[i]) + carry
        if int(x1[i]) == p:
            k += q - p
        res = res + str(k%10)
        carry = k//10
        i += 1
    while j < len2:
        k = int(x2[j]) + carry
        if int(x2[j]) == p:
            k += q - p
        res = res + str(k%10)
        carry = k//10
        j += 1
    if carry > 0:
        res = res + "1"
    return int(res[::-1])

test = int(input())
while test > 0:
    test -= 1
    a, b = [int(i) for i in input().split(' ')]
    x1 = ""
    x2 = ""
    A = [str(s) for s in input().split(' ')]
    for s in A:
        if s != '':
            if x1 =="":
                x1 = s
            else: x2 = s
        if x2 != "": break
    if x2 == "":
        x2 = str(input())
    x1 = x1[::-1]
    x2 = x2[::-1]
    s1 = sumIf(x1, x2, a, b)
    s2 = sumIf(x1, x2, b, a)
    print(str(s1) + ' ' + str(s2) if s1 < s2 else str(s2) + ' ' + str(s1))