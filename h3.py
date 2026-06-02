def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
    

text = input("შემოიყვანე რიცხვი : ")

if text.isdigit():
    print(fibonacci(int(text)))
else:
    print("შემოიყვანე მხოლოდ რიცხვი..")