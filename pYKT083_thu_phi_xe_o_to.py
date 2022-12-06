from collections import OrderedDict
def getCost(record):
    if record[1] == "Xe_con":
        if record[2] == "5":
            return 10000
        return 15000
    if record[1] == "Xe_tai":
        return 20000
    if record[2] == "29":
        return 50000
    return 70000


costList = OrderedDict()
amount = int(input())
for i in range(amount):
    record = input().split()
    if record[3] == "IN":
        if record[4] not in costList:
            costList.update({record[4]: getCost(record)})
        else:
            costList[record[4]] += getCost(record)

for key in costList:
    print(key, costList[key], sep=": ")
# 5
# 30F-123.15 Xe_con 5 OUT 06/11/2021
# 30F-123.15 Xe_con 5 IN 06/11/2021
# 30H-123.15 Xe_con 7 IN 06/11/2021
# 29H-222.68 Xe_tai 2 IN 07/11/2021
# 30G-511.15 Xe_con 5 IN 07/11/2021