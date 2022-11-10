
sa, sb = input().split()
a = set()
b = set()
for i in input().split():
    a.add(int(i))
for i in input().split():
    b.add(int(i))
union = a.union(b)
x = a.difference(b)
y = b.difference(a)
common = union.difference(x.union(y))
print(*sorted(common))
print(*sorted(x))
print(*sorted(y))