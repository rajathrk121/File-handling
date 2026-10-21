with open ('attendence.txt','r') as source:
    data=source.read()

with open('copy.txt','w') as destination:
    destination.write(data)
