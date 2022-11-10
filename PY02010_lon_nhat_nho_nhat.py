import fileinput

while True:
    test = int(input())
    if test == 0:
        break
    arr = []
    while test > 0:
        test -= 1
        arr.append(int(input()))
    if max(arr) == min(arr):
        print("BANG NHAU")
    else: print(min(arr), max(arr), sep=' ')