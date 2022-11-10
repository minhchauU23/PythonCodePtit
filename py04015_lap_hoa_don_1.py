

from decimal import Decimal


class Bill:
    counter = 1
    def __init__(self, name, waterBlock):
        self.id = 'KH%02d'%Bill.counter
        self.name = name
        self.waterBlock = waterBlock
        Bill.counter += 1

    def getPrice(self):
        water = self.waterBlock
        res = 0
        if water > 100:
            res += (water - 100) * 200
            water = 100
        if water > 50:
            res += (water - 50) * 150
            water = 50
        res += water * 100
        return res

    def getExtraFee(self):
        if self.waterBlock > 100:
            return  Decimal('0.05')*self.getPrice()
        if self.waterBlock > 50:
            return Decimal('0.03')*self.getPrice()
        return Decimal('0.02')*self.getPrice()
    
    def getTotal(self):

        return Decimal.quantize(self.getPrice() + self.getExtraFee(), 0)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.getTotal())

billList = []
amount = int(input())
for i in range(amount):
    billList.append(Bill(input(), -Decimal(input())+ Decimal(input())))
print(*sorted(billList, key = lambda item : -item.getTotal()), sep='\n')
# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612