import sys

sys.setrecursionlimit(10**4)

def merge(arr, l, mid, r):
    i = l
    j = mid + 1
    newArr = []
    cnt = 0
    while i <= mid and j <= r:
        if arr[i] > arr[j]:
            newArr.append(arr[j])
            cnt += (mid - i + 1)
            j += 1
        else:
            newArr.append(arr[i])
            i += 1
    while i <= mid:
        newArr.append(arr[i])
        i += 1
    while j <= r:
        newArr.append(arr[j])
        j += 1
    for id in range(l, r + 1):
        arr[id] = newArr[id - l]
    return cnt
def mergeSort(arr, l, r):
    if l < r:
        mid = (l + r)//2
        x = mergeSort(arr, l, mid)
        y = mergeSort(arr, mid+1, r)
        return merge(arr, l, mid, r) + x + y
    return 0

sz = int(input())
arr = [int(i) for i in input().split()]
print(mergeSort(arr, 0, sz - 1))

