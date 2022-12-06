
n, m = [int(i) for i in input().split()]
candidates = [0 for i in range(m)]
maxVote = -1
secondVote = 0
for i in input().split():
    candidates[int(i)-1] += 1
    maxVote = max(maxVote, candidates[int(i)-1])

for i in range(len(candidates)):
    if candidates[i] < maxVote:
        if secondVote == -1 or candidates[secondVote] < candidates[i]:
            secondVote = i

if secondVote == 0:
    print("NONE")
else: print(secondVote + 1)
# 10 4
# 2 3 1 2 3 4 1 2 3 2
# 8 4
# 1 2 3 4 4 3 2 1
