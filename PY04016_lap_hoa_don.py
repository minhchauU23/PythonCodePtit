from datetime import datetime

class Customer:
    counter = 1
    def __init__(self, name, idRoom, checkInDate, checkOutDate, extraCost):
        self.cID = "KH%02d"%Customer.counter
        Customer.counter += 1
        self.name = name
        self.idRoom = idRoom
        self.checkInDate = datetime.strptime(checkInDate, "%d/%m/%Y")
        self.checkOutDate = datetime.strptime(checkOutDate, "%d/%m/%Y")
        self.extraCost = int(extraCost)
    def getStayedDates(self):
        diff = self.checkOutDate - self.checkInDate
        return diff.days + 1
    def getUnitPrice(self):
        if self.idRoom[0] == "1":
            return 25
        if self.idRoom[0] == "2":
            return 34
        if self.idRoom[0] == "3":
            return 50
        return 80
    def getCost(self):
        return self.getUnitPrice()*self.getStayedDates()
    def getTotalCost(self):
        return  self.extraCost + self.getCost()
    def __str__(self):
        return "{} {} {} {} {}".format(self.cID, self.name, self.idRoom, self.getStayedDates(), self.getTotalCost())

numOfCustomers = int(input())
customers = []
for i in range(numOfCustomers):
    customer = Customer(input().strip(), input().strip(), input().strip(), input().strip(), input().strip())
    customers.append(customer)
customers = sorted(customers, key=lambda cs: -cs.getTotalCost())
print(*customers, sep="\n")
# 3
# Huynh Van Thanh
# 103
# 05/06/2010
# 05/06/2010
# 15
# Le Duc Cong
# 106
# 08/03/2010
# 01/05/2010
# 220
# Tran Thi Bich Tuyen
# 207
# 10/04/2010
# 21/04/2010
# 96