
nbOfLine = int(input())
line = input().split()
cnt = [0, 0]
state = len(line) % 2
cnt[len(line) % 2] += 1
res = []
for i in range(1, nbOfLine):
    line = input().split()
    kind = len(line) % 2
    if kind != state:
        if state == 0:
            res.append(state + 1)
        else:
            for j in range(cnt[state]//4):
                res.append(state + 1)
        cnt[state] = 0
        state = kind
    cnt[kind] += 1
if state == 0:
    res.append(state + 1)
else:
    for j in range(cnt[state] // 4):
        res.append(state + 1)
print(len(res))
print(*res, sep='\n')
# 12
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay