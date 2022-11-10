
sz1, sz2 = input().split()
arr1 = set(input().split())
arr2 = set(input().split())

if(sorted(arr1) == sorted(arr2)): print("YES")
else: print("NO")