note=input("Input notes: ")
a=open('notes.txt','w')
a.write(note)
a.close()

note=input("Input notes: ")
b=open('notes.txt','a')
b.write('\n'+note)
b.close()