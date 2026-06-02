import random

name=input("შემოიყვანე სახელი")
l1=["Super","Great","Player","N1","Slay"]

print(random.choice(l1)+name)
print(name+str(random.choice(l1)))
print(name+str(random.randint(1,10000)))
print(name+name+str(random.randint(1,100)))
print(random.choice(l1)+name+str(random.randint(1,10000)))
