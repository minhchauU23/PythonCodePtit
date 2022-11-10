
st = set()
amount = 0
while amount < 10:
    s = input()
    for i in s.split():
        amount += 1
        st.add(int(i) % 42)
print(len(st))    

