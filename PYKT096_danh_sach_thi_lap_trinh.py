# 03

class Team:
    counter = 1
    def __init__(self, nameT, nameUni):
        self.id = "Team%02d"%Team.counter
        self.nameT = nameT
        self.nameUni = nameUni
        Team.counter += 1
    def __str__(self):
        return  "{} {}".format(self.nameT, self.nameUni)

class Candidate:
    counter = 1
    def __init__(self, name, teamID):
        self.id = "C%03d"%Candidate.counter
        self.name = name
        self.teamID = teamID
        Candidate.counter += 1

    def setTeam(self, team):
        self.team = team

    def __str__(self):
        return "{} {} {}".format(self.id, self.name, self.team)

numOfTeams = int(input())
teams = dict()
for i in range(numOfTeams):
    team = Team(input(), input())
    teams.update({team.id:team})

numOfCandidate = int(input())
examinees = []
for i in range(numOfCandidate):
    examinee = Candidate(input(), input())
    examinee.setTeam(teams[examinee.teamID])
    examinees.append(examinee)
examinees = sorted(examinees, key= lambda ex: ex.name)
print(*examinees, sep= "\n")
# 2
# BAV_MIS
# Banking Academy of Vietnam
# FTU Knights1
# Foreign Trade University
# 6
# Le Trung Toan
# Team01
# Nguyen Trinh Quoc Long
# Team01
# Giang Minh Tung
# Team01
# Nguyen Hang Giang
# Team02
# Nguyen Thanh Nhan
# Team02
# Nguyen Viet Duc
# Team02