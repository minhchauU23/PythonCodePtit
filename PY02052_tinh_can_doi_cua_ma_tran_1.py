n = int(input())
above = 0
under = 0
for row in range(n):
    arr = [int(i) for i in input().split()]
    above += sum(arr[row+1::])
    under += sum(arr[0:row])
k = int(input())
print(f"YES \n{abs(above-under)}" if abs(above-under) <= k else f"NO \n{abs(above-under)}" )
# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5