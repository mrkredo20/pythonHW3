import random

length = int(input("Enter length: "))
inputs=""
answers=[
    input("Include lowercase letters? y/n: "),
    input("Include uppercase letters? y/n: "),
    input("Include numbers? y/n: "),
    input("Include symbols? y/n: ")
]

for t in answers:
    if not t.isascii():
        print("შეიყვანე მხოლოდ ლათინური ასოები")
        exit()

if answers[0].lower() == "y":
    inputs += "abcdefghijklmnopqrstuvwxyz"

if answers[1].lower() == "y":
    inputs += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if answers[2].lower() == "y":
    inputs += "0123456789"

if answers[3].lower() == "y":
    inputs += "!@#$%^&*()_+-=[]"

if inputs == "":
    print("აირჩიე მინიმუმ ერთი ტიპი")
else:
    password = ""
    for i in range(length):
        password += random.choice(inputs)
    print("Generated password:",password)