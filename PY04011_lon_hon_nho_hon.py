import sys
sys.setrecursionlimit(10**6)
G = dict()
TG = dict()
visited = [False for i in range(2* 10**5)]

def DFS1(u):
    for v in range(G[u]):
        if visited




sz = int(input())
ok = True
for i in range(sz):
    operation = input().split()
    person1 = operation[0]
    person2 = operation[2]
    if operation[1] == "<":
        person1 = operation[2]
        person2 = operation[0]
    if person1 in G:
        G[person1].append(person2)
    else:
        G.update({person1: [person2]})
    if person2 in TG:
        TG[person2].append(person1)
    else:
        TG.update({person2: [person1]})



# 3
# An > Binh
# Binh > Cong
# An > Cong