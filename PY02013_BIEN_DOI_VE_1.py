
while True:
    n = int(input())
    if n == 0: break
    st = set()
    st.add(n)
    while n > 1:
        if n % 2 == 0:
            n/=2
        else: n = n * 3 + 1
        st.add(n)
    print(len(st))