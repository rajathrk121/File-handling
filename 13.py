name=input("Enter the name of the student: ")
found=True
with open("students.txt",'r') as s:
    for i in s.readlines():
        if name in i:
            print(name,'found in file')
            found=True
            break
        else:
            found=False

if found ==False:
    print(name,'not found')
    
        