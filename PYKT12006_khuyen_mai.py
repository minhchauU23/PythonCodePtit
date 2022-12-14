
n, k = [int(i) for i in input().split()]
preSale = [int(i) for i in input().split()]
both = []
id = 0
for i in input().split():
    both.append([preSale[id], int(i)])
    id += 1
both = sorted(both, key=lambda it: [it[0]-it[1], it[0]])

cost = 0
for i in range(k):
    cost += both[i][0]
for i in range(k, n):
    if both[i][0] < both[i][1]:
        cost += both[i][0]
    else:
        cost += both[i][1]

print(cost)