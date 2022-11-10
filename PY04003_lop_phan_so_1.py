import math


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def shorten(self):
        x = math.gcd(self.numerator, self.denominator)
        self.numerator //= x
        self.denominator //= x
    
    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

if __name__ == '__main__':
    arr = input().split()
    fr = Fraction(int(arr[0]), int(arr[1]))
    fr.shorten()
    print(fr)    