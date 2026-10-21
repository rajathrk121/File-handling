count=int(input('Enter the number of students: '))
with open ('student.txt','w') as s:
    for i in range(count):
        Name=input(f"Enter name of the student {i+1}: ")
        s.write(Name+'\n')
with open('student.txt', 'r') as s:
    data=s.read()
    print(data)