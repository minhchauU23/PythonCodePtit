
import operator


class Student:
    def __init__(self, name, accept, submit):
        self.name = name
        self.accept = accept
        self.submit = submit
    def __str__(self):
        return '{} {} {}'.format(self.name, self.accept, self.submit)



studentList = []
size = int(input())
while size > 0:
    size -= 1
    name = input()
    arr = input().split()
    studentList.append(Student(name, int(arr[0]), int(arr[1])))
for std in sorted(studentList, key=lambda item : (-item.accept, item.submit, item.name)):
    print(std)

# 2
# Nguyen Van Nam
# 169 599
# Tran Thi Ngoc
# 168 600