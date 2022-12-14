
def count(arr, leftMax, sz):
     if sz == 1:
          return  1
     cnt = 0
     if arr[sz - 1] >= leftMax[sz-2]:
          cnt += 1
     rightMin = arr[sz - 1]
     for i in range(sz - 2, 0, -1):
          if arr[i] < rightMin and arr[i] >= leftMax[i-1]:
               cnt += 1
          rightMin = min(rightMin, arr[i])
     if arr[0] < rightMin:
          cnt += 1
     return cnt


test = int(input())
while test > 0 :
     test -= 1
     sz = int(input())
     arr = [int(i) for i in input().split()]
     leftMax = [0 for i in range(sz)]
     leftMax[0] = arr[0]
     for i in range(1, sz):
          leftMax[i] = max(arr[i], leftMax[i-1])
     print(count(arr, leftMax, sz))
