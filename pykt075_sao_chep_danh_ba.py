class Person:
    def __init__(self, firstName, lastName, phone, date):
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.date = date
    def __str__(self):
        return "{} {} {} {}".format(self.firstName, self.lastName + ":", self.phone, self.date)

ip = open("SOTAY.txt")
op = open("DIENTHOAI.txt", "w")
date = ip.readline().split()
persons = []
while True:
    line = ip.readline().split()
    if len(line) == 0: break
    if line[0] == "Ngay":
        date = line
        continue
    lastName = line[-1]
    firstName = ""
    for i in range(0, len(line) - 1):
        firstName += line[i] + " "
    firstName.strip()
    phone = ip.readline()
    persons.append(Person(firstName.strip(), lastName.strip(), phone.strip(), date[-1].strip()))
persons = sorted(persons, key = lambda ps: (ps.lastName, ps.firstName))
for ps in persons:
    s = ps.__str__()
    op.write(str(s) + "\n")
ip.close()
op.close()


