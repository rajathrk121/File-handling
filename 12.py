word=input('Enter word: ').lower()

with open('notes.txt','r') as n:
    count=0
    data=n.read().lower()
    words=data.split()
    for i in words:
        if word == i:
            count+=1

    if count==0:
        print(word , 'not found')


print(word,':',count)