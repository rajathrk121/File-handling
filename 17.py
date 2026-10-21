with open('students.txt','a')as s:
    total_mark=0
    
    for i in range(3):
        name=input("Enter name: ")
        mark=int(input("Enter mark: "))
        s.write(name+':'+str(mark)+'\n')
        
        total_mark+=mark

    average=total_mark/3

print('Average mark: ',average)

stu_up=[]

with open ('students.txt',"r") as s:
    data=s.read()
    if mark>average:
        print(name ,':',mark)
    