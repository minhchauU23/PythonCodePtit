
s = input()
st = set()
for i in range(0, len(s), 2):
    x = int(s[i:min(i+2, len(s))])
    if x > 9:
        st.add(x)
print(*sorted(st))