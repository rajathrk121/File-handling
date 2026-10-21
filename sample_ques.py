# num=int(input('Enter number of the students: '))

# for i in range(num):
#     name=input(f'Enter name of student {i+1}: ')
#     age=int(input(f"Enter age of the student: "))

#     with open('student.txt','a') as a:
#         a.write('Name: '+name+', Age: '+str(age)+'\n')

# with open('student.txt','r') as d:
#     data=d.read()

#     print("All students")

#     print(data)

name=input('Enter name of the student: ')

with open('student.txt','r') as a:
    data=a.read()
    while True:
        if name in data:
            print('Match found: ',name)
            break
        else:
            print('Match not found')
            break