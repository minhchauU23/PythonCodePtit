
line1 = set(str.lower(input()).split())
line2 = set(str.lower(input()).split())

union = line1.union(line2)
common = line2.difference(union.difference(line1))
print(*sorted(union), sep=" ")
print(*sorted(common), sep = " ")