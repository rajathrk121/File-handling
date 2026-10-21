with open('student.txt','a') as s:
    for i in range(5):
        name=input("Enter name of student: ")
        age=int(input('Enter age: '))
        course=input("Enter Course name: ")
        mark=int(input("Enter mark: "))

        s.write('Name: '+name+ '\n'+'Age: '+str(age)+'\n'+'Course: '+course+'\n' 'Mark: '+str(mark) +'\n\n')