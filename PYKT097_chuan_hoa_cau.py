import fileinput

res = ""
words = ""
# f = open("test.txt", "r+")
f = fileinput.input()
while True:
    line = f.readline()
    if line == "":
        break
    for word in line.lower().split():
        for char in word:
            if char == "." or char == "!" or char == "?":
                words = words.strip()+ char
                res += words
                res += "\n"
                words = ""
            elif char == "\n":
                continue
            else:
                if words == "":
                    words += char.upper()
                else:
                    words += char
        if words != "":
             words += " "
    if words != "":
        words = words.strip() + "."
        res += words + "\n"
        words = ""
print(res, end="")
# Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.
# co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
# muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
# moi    CAC BAN danG ky     thaM giA !