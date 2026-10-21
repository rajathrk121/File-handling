note=input("Enter notes: ")
with open('notes.txt','a') as a:
    a.write('\n'+note)

with open ('notes.txt','r') as b:
    c=b.read()
    print(c)
