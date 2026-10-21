with open('student.txt','a') as s:
    Name=input('Enter name of the student: ')
    Course=input("Enter course name: ")
    College=input("Enter name of the college: ")
    Year=int(input("Enter pass out year: "))

    s.write('\n'+'Name: '+ Name + '\n' + 'Course: '+ Course +'\n' + 'College: ' + College + '\n' + 'Year: ' + str(Year))
