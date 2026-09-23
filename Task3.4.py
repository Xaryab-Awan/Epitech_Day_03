text=input("ENTER A STRING: ")
words=text.split()
newword=""
for i in range(len(words)):
    newword+=words[i][0]

print(newword)