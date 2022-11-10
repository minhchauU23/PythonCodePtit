

res = 0

def merge(l, mid, r, arr):
    leftArr = arr[l:mid + 1]
    rightArr = arr[mid + 1 : r + 1]
    index = l
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if rightArr[rightIndex] < leftArr[leftIndex]:
            arr[index] = leftArr[leftIndex] 
            leftIndex += 1
            global res
            res += len(rightArr) - rightIndex
        else:
            arr[index] = rightArr[rightIndex]
            rightIndex += 1
        index+=1
    while leftIndex < len(leftArr):
        arr[index] = leftArr[leftIndex] 
        leftIndex += 1
        index += 1
    while rightIndex < len(rightArr):
        arr[index] = rightArr[rightIndex]
        rightIndex += 1
        index += 1


def mergeSort(l, r, arr):
    if(l < r):
        mid = (l + r)//2
        mergeSort(l, mid, arr)
        mergeSort(mid + 1, r, arr)
        merge(l, mid, r, arr)

size = int(input())
arr = [int(i) for i in input().split()]
mergeSort(0, size - 1, arr)
print(res)