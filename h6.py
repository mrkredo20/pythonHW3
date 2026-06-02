import random
length=int(input("რანდემი რიცხვი შემოგყავს?: "))
l=[]
for i in range(length):
    x=int(input(f"შემოიყვანე {i+1} რიცხვი: "))
    l.append(x)
    
sorting=int(input("როგორ დავასორტიროთ?აირჩიე შესაბამისი ციფრი 1. ზრდადობით 2.კლებადობით 3.უნიკალურები 4. რენდომად"))
if sorting==1:
    print(sorted(l))
elif sorting==2:
    print(sorted(l,reverse=True))
elif sorting==3:
    print(set(l))
elif sorting==4:
    random.shuffle(l)
    print(l)
else:
    print("შემოიყვანე სწორი ციფრი")