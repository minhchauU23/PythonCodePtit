import datetime
typeMovies = dict()
movies = []

class Movies:
    counter = 1
    def __init__(self, typeId, date, name, episodes):
        self.id = "P%03d"%Movies.counter
        self.typeMv = typeMovies[typeId]
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y")
        self.name = name
        self.episodes = episodes
        Movies.counter += 1
    def __str__(self):
        return "{} {} {} {} {}".format(self.id, self.typeMv, self.date.strftime("%d/%m/%Y"), self.name, self.episodes)



numberOftypes, numberOfMovies = [int(i) for i in input().split()]

for i in range(numberOftypes):
    typeMovies.update({"TL%03d"%(i + 1): input().strip()})


for i in range(numberOfMovies):
    movies.append(Movies(input().strip(), input().strip(), input().strip(), int(input())))

movies = sorted(movies, key=lambda mv:(mv.date, mv.name, -mv.episodes))
print(*movies, sep= "\n")
# 2 3
# Hai huoc
# Tinh cam
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5