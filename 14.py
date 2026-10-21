with open('students.txt','w') as s:
    student={}
    
    
    for i in range(5):
        name=input("Enter the name of student: ")
        mark=int(input("Enter mark: "))
        s.write('Name: '+name+'\n'+"Mark: "+str(mark)+'\n' )

        if mark>50:
            student[name]=mark

print(student)


    