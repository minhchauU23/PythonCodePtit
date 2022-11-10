
def check(arr1, arr2):
    for i in range(0, len(arr1)):
        if(arr1[i] > arr2[i]) : 
            return False
    return True; 

test = int(input())
while test > 0:
    test -=1
    size = int(input())
    firstArray = [int(i) for i in input().split()]
    secondArray = [int(i) for i in input().split()]
    print("YES" if check(sorted(firstArray), sorted(secondArray)) else "NO") 
