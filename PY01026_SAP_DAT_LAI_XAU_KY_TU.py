
test = int(input())
for i in range(1, test + 1):
    str1 = str(input())
    str2 = str(input())
    print(f"Test {i}:", end = " ")
    if(len(str1) != len(str2) or sorted(str1) != sorted(str2)):
        print("NO")
    else: print("YES")