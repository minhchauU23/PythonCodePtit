questions = {}
amount = int(input())
type = ''
cnt = 0
for i in range(amount):
    line = input()
    if type == '':
        type = line
        continue
    elif line == '':
        if questions.get(type) is None:
            questions.update({type: cnt})
        else:
            questions[type] = questions[type] + cnt
        type = ''
        cnt = 0
    else:
        cnt+=1
if type != '':
    if questions.get(type) is None:
            questions.update({type: cnt})
    else:
        questions[type] = questions[type] + cnt
for i in questions:
    print('{}: {}'.format(i, questions[i]))

# 9
# Home/accommodation
# What kind of housing/accommodation do you live in?
# Who do you live with?
# How long have you lived there?

# Study
# Describe your education
# What is your area of specialization?
# Why did you choose to study that major?