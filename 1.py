Name=input('Enter name of the student: ')
Course=input("Enter course name: ")
College=input("Enter name of the college: ")
Year=int(input("Enter pass out year: "))

with open('student.txt','w') as s:
    s.write('Name: '+ Name + '\n' + 'Course: '+ Course +'\n' + 'College: ' + College + '\n' + 'Year: ' + str(Year))
