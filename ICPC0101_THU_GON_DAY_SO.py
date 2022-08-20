

size = int(input())
numbers = []

x = [int(x) for x in input().split()]
for item in x:
    if len(numbers) == 0 or (numbers[len(numbers)-1] + item) % 2 != 0:
        numbers.append(item)
    else:
        numbers.pop(len(numbers) - 1)
print(len(numbers))

