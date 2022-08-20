
cnt = 0

str = input()

for index in range(len(str)):
    if str[index] == '4' or str[index] == '7':
        cnt += 1

print("YES" if cnt == 4 or cnt == 7 else "NO")