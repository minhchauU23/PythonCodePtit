from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def shorten(self):
        GCD = gcd(self.denominator, self.numerator)
        self.numerator //= GCD
        self.denominator //= GCD
    def add(self, secondFraction):
        self.numerator = self.numerator * secondFraction.denominator + self.denominator * secondFraction.numerator
        self.denominator *= secondFraction.denominator
    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

if __name__ == '__main__':
    arr = input().split()
    fr1 = Fraction(int(arr[0]), int(arr[1]))
    fr2 = Fraction(int(arr[2]), int(arr[3]))
    fr1.add(fr2)
    fr1.shorten()
    print(fr1) 