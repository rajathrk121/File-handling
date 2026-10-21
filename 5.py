with open ('student.txt','r') as s:
    data=s.read()
    text=data.split()
    word=0

    for words in text:
        word+=1

print(word)