count=int(input('Enter the number of students: '))

with open ('attendence.txt','a') as s:
    for i in range (count):
        name=input("Enter student name: ")
        attend=input("Enter attendence status (Present/Absent): ")

        s.write('\n\n'+'Name: '+name + '\n'+'Attendence: '+attend)

with open ('attendence.txt','r') as s:
    data=s.read()
    print(data)