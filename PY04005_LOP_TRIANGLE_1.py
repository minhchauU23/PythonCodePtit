from decimal import ROUND_05UP, ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR, Decimal
import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self, p):
        dis  = math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2) 
        return dis

class Triangle:
    def __init__(self, firstPoint, secondPoint, thirdPoint):
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint
        self.thirdPoint = thirdPoint
    def getValid(self):
        firstEdge = self.firstPoint.distance(self.secondPoint)
        secondEdge = self.firstPoint.distance(self.thirdPoint)
        thirdEdge = self.secondPoint.distance(self.thirdPoint)
        if firstEdge + secondEdge > thirdEdge and firstEdge + thirdEdge > secondEdge and secondEdge + thirdEdge > firstEdge:
            return True
        return False  
    def getPerimeter(self):
        firstEdge = self.firstPoint.distance(self.secondPoint)
        secondEdge = self.firstPoint.distance(self.thirdPoint)
        thirdEdge = self.secondPoint.distance(self.thirdPoint)
        return round((firstEdge + secondEdge + thirdEdge)*1000)*0.001
t = int(input())
while t > 0:
    arr = input().split()
    while len(arr) < 6:
        for i in input().split():
            arr.append(i)
            if len(arr) == 6:
                break
    triangle = Triangle(Point(float(arr[0]), float(arr[1])), Point(float(arr[2]), float(arr[3])), Point(float(arr[4]), float(arr[5])))
    if triangle.getValid():
        print(triangle.getPerimeter())
    else: print("INVALID") 
    t -= 1