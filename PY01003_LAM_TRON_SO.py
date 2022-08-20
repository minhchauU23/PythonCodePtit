

from math import remainder
import string
from tokenize import String


def round(number):
    val = 10
    while number > val:
        rmd = number%val
        if rmd >= val/2: 
            number = number+val - rmd
        else: 
            number = number - rmd
        val *= 10
    return number
    

def Test():
    numOfTest = int(input())
    for test in range(numOfTest):
        number = int(input())
        print(round(number))

Test()