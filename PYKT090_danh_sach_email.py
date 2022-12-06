
file = open("CONTACT.in", "r")
emails = []
while True:
    email = file.readline().lower().strip()
    if email == "":
        break
    emails.append(email.lower())

emails = sorted(set(emails))
for email in emails:
    print(email)
