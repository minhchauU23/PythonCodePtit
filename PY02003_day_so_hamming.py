hamming = [1]
def generate():
    pos2 = 0
    pos3 = 0
    pos5 = 0
    while True:
        hmNum = min(hamming[pos2] * 2, min(hamming[pos3] * 3, hamming[pos5] * 5))
        if hmNum > 10e18:
            return
        if hamming[pos2] * 2 == hmNum:
            pos2 += 1
        if hamming[pos3] * 3 == hmNum:
            pos3 += 1
        if hamming[pos5] * 5 == hmNum:
            pos5 += 1
        hamming.append(hmNum)

def binarySearch(arr,  value):
    left = 0
    right = len(arr) - 1
    if value > arr[right] or value < arr[left]:
        return -1
    while left <= right:
        mid = (right - left)//2 + left
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return -1

generate()
test = int(input())
while test > 0:
    test -= 1
    checkNum = int(input())
    index = binarySearch(hamming, checkNum)
    print((index + 1) if index > -1 else "Not in sequence")