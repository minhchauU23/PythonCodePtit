from collections import deque

def generate(size):
    queue = deque()
    queue.append(("2", (True, False, False, False)))
    queue.append(("3", (False, True, False, False)))
    queue.append(("5", (False, False, True, False)))
    queue.append(("7", (False, False, False, True)))
    while len(queue) > 0:
        left = queue.popleft()
        if len(left[0]) >= 4 and len(left[0]) <= size and left[0][-1] != "2" and left[1][0] == left[1][1] and left[1][1] == left[1][2] and left[1][2] == left[1][3]:
            print(left[0])
        if len(left[0]) < size:
            queue.append((left[0] + "2", (True, left[1][1], left[1][2], left[1][3])))
            queue.append((left[0] + "3", (left[1][0], True, left[1][2], left[1][3])))
            queue.append((left[0] + "5", (left[1][0], left[1][1], True, left[1][3])))
            queue.append((left[0] + "7", (left[1][0], left[1][1], left[1][2], True)))

generate(int(input()))