with open('student.txt','r') as s:
    count=0
    for r in s.readlines():
        count+=1

print(count)