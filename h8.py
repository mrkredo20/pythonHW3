length=int(input("რანდემი რიცხვი შემოგყავს?: "))
l=[]
for i in range(length):
    x=int(input(f"შემოიყვანე {i+1} რიცხვი: "))
    l.append(x)
while l:
    print(l)
    new_l=[]
    for i in range(len(l) - 1):
        new_l.append(l[i] + l[i+1])
    l = new_l

