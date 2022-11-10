class Rectangle:
    def __init__(self, height, width, colors):
        self.height = height
        self.width = width    
        self.colors = colors
    def perimeter(self):
        return (self.height + self.width) * 2
    def area(self):
        return self.height *  self.width
    def color(self):
        return self.colors.title()

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")
