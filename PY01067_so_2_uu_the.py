arr = []
def generate():
    queue = ["1", "2"]
    while len(arr) < 1000:
        nb = queue[0]
        queue.pop(0)
        if nb.count('2') > len(nb)//2:
            arr.append(nb)
        queue.append(nb + "0")
        queue.append(nb + "1")
        queue.append(nb + "2")

generate()
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    print(*arr[:n])
