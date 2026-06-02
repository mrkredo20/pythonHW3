word=input("შემოიყვანე სიტყვა")
new_word=""
for i in word:
    if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZაბგდევზთიკლმნოპჟრსტუფქღყშცძწჭხჯჰ ":
        new_word+=i
print(new_word)