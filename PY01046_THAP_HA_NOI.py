def recursion(A, B, C, n):
    if n == 1:
        print(A + ' -> ' + C)
        return
    # print(B + '->' + C)
    recursion(A, C, B, n-1)
    recursion(A, B, C, 1)
    recursion(B, A, C, n-1)

n = int(input())
recursion('A', 'B', 'C', n)
