size = [1]
for i in range(1, 25):
    size.append(size[i-1] * 2 + 1)


def charAt(n, k):
    if n == 0: return 'A'
    if k == size[n-1] + 1: return chr(ord('A') + n)
    if k > size[n-1]:
        return charAt(n - 1, k - size[n-1] - 1)
    return charAt(n-1, k)


test = int(input())
while test > 0:
    test -= 1
    n, k = input().split()
    print(charAt(int(n) - 1, int(k)))


