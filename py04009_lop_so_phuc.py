
test = int(input())
while test > 0:
    test -= 1
    arr = [int(i) for i in input().split()]
    cp1 = complex(arr[0], arr[1])
    cp2 = complex(arr[2], arr[3])
    c = (cp1 + cp2)*cp1
    d = (cp1 + cp2)**2
    print('{} + {}i'.format(int(c.real), abs(int(c.imag))) if int(c.imag) > 0 else '{} - {}i'.format(int(c.real), abs(int(c.imag))), end = ', ')
    print('{} + {}i'.format(int(d.real), abs(int(d.imag))) if int(d.imag) > 0 else '{} - {}i'.format(int(d.real), abs(int(d.imag))))
