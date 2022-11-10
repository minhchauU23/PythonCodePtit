def sum(nb):
    sm =0
    for i in range(len(nb)):
        sm += ord(nb[i]) - ord('0')
    return str(sm)

def count(nb):
    counter = 0
    while len(nb) > 1:
        nb = sum(nb)
        counter += 1
    return counter


nb = str(input())
print(count(nb))