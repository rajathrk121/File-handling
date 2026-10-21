name=input("Enter Your Name: ")
age=int(input("Enter your age: "))
place=input("Enter your place: ")

a=open('student.txt','w')
a.write(name+'\n'+str(age)+'\n'+place)
a.close()

b=open ('student.txt','r')
c=b.read()
print(c)
b.close()


