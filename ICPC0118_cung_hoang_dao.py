def convert(date, month):
    if month == 1:
        return "Ma Ket" if date <= 19 else "Bao Binh"
    if month == 2:
        return "Bao Binh" if date <= 18 else "Song Ngu"
    if month == 3:
        return "Song Ngu" if date <= 20 else "Bach Duong"
    if month == 4:
        return "Bach Duong" if date <= 19 else "Kim Nguu"
    if month == 5:
        return "Kim Nguu" if date <= 20 else "Song Tu"
    if month == 6:
        return "Song Tu" if date <= 20 else "Cu Giai"
    if month == 7:
        return "Cu Giai" if date <= 22 else "Su Tu"
    if month == 8:
        return "Su Tu" if date <= 22 else "Xu Nu"
    if month == 9:
        return "Xu Nu" if date <= 22 else "Thien Binh"
    if month == 10:
        return "Thien Binh" if date <= 22 else "Thien Yet"
    if month == 11:
        return "Thien Yet" if date <= 22 else "Nhan Ma"
    if month == 12:
        return "Nhan Ma" if date <= 21 else "Ma Ket"

test = int(input())
while test > 0:
    test -= 1
    date, month = [int(i) for i in input().split()]
    print(convert(date, month))