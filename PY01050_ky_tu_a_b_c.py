from collections import deque
def generate(length):
    queue = deque()
    queue.append(('A', 0, 0))
    queue.append(('B', 1, 0))
    queue.append(('C', 0, 1))
    while len(queue) > 0:
        pr = queue.popleft()
        lenC = pr[2]
        lenB = pr[1]
        lenA = len(pr[0]) - lenB - lenC
        if lenA + lenB + lenC >= 3 and lenC >= lenB and lenB >= lenA and lenA > 0:
            print(pr[0])
        if len(pr[0]) < length:
            queue.append((pr[0] + 'A', pr[1], pr[2]))
            queue.append((pr[0] + 'B', pr[1] + 1, pr[2]))
            queue.append((pr[0] + 'C', pr[1], pr[2] + 1))
length = int(input())
generate(length)