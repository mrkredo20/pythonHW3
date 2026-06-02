password = input("პაროლი: ")
score = 0

if len(password)>= 8:  score += 1

for x in password:
    if x.isdigit():  score += 1; break
for x in password:
    if x.isupper():  score += 1; break
for x in password:
    if x.islower():  score += 1; break
for x in password:
    if x in "!@#$%^&*": score += 1; break

if len(password) != len(set(password)): score -= 1

if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")
