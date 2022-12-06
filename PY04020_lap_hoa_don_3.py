
class Bill:
    def __init__(self, id, nameProduct, quantity, unitPrice, discount):
        self.id = id
        self.nameProduct = nameProduct
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.discount = discount
    def getCost(self):
        return  self.unitPrice * self.quantity - self.discount
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.id, self.nameProduct, self.quantity, self.unitPrice, self.discount, self.getCost())

nbOfBills = int(input())
bills = []
for i in range(nbOfBills):
    bills.append(Bill(input().strip(), input().strip(), int(input().strip()), int(input().strip()), int(input().strip())))

bills = sorted(bills, key=lambda it: -it.getCost())
print(*bills, sep="\n")

# 3
# ML01
# May lanh SANYO
# 12
# 4000000
# 2400000
# ML02
# May lanh HITACHI
# 4
# 2550000000
# 0
# ML03
# May lanh NATIONAL
# 5
# 3000000
# 150000