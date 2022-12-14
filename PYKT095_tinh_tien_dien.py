
class Bill:
    counter = 1
    dm = [100, 500, 200]
    def __init__(self, name, typeU, start, end):
        self.id = "KH%02d"%Bill.counter
        self.name = name
        self.typeU = typeU
        self.start = start
        self.end = end
        Bill.counter += 1

    def getUseElectric(self):
        return self.end - self.start

    def getInCost(self):
        if self.getUseElectric() < Bill.dm[ord(self.typeU) - ord("A")]:
            return self.getUseElectric() * 450
        else:
            return Bill.dm[ord(self.typeU) - ord("A")] * 450
    def getOutCost(self):
        if self.getUseElectric() <= Bill.dm[ord(self.typeU) - ord("A")]:
            return 0
        else:
            return (self.getUseElectric() - Bill.dm[ord(self.typeU) - ord("A")]) * 1000

    def getVAT(self):
        return self.getOutCost()//20

    def getCost(self):
        return self.getInCost() + self.getOutCost() + self.getVAT()

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.id, self.name, self.getInCost(), self.getOutCost(), self.getVAT(), self.getCost())


nbBills = int(input())
bills = []
for i in range(nbBills):
    n = input().title().split()
    a = input().split()
    name = ""
    for i in n:
        name += i + " "
    bills.append(Bill(name.strip(), a[0], int(a[1]), int(a[2])))

bills = sorted(bills, key= lambda b: -b.getCost())
print(*bills, sep= "\n")
# 2
#  nGuyEn Hong Ngat
# C 200 278
#  Chu thi    minh
# A 120 160