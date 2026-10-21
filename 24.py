def add():
    with open('student.txt','a') as s:
        name=input("Enter name of the student: ")
        course=input("Enter course name: ")
        mark=int(input("Enter mark: "))

        s.write('Name: '+name+'\n'+'Course: '+course+'\n'+'Mark: '+str(mark)+'\n\n')

def view():
    with open('student.txt','r') as s:
        data=s.read()
        print(data)

def search():
    s_name=input('Enter name of the sudent: ')

    with open ('student.txt','r') as s:
        data=s.read()
        students=data.split('\n\n')
        found=False
        for student in students:

            if 'Name: '+s_name+'\n' in student:
                print(student)
                found=True
                break

    if not found:
        print("Student not found")

def stop():
    print("Exitinggg.....")
    exit()

while True:
    choice=input("Enter your choice(add_student/view_student/search_student/exit)")

    match choice:
        case 'add_student':
            add()

        case 'view_student':
            view()
        case 'search_student':
            search()
        case 'exit':
            stop()
            break
        case _:
            print("Enter a valid choice")