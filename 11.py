word=input("Enter word you wanna to search: ")
with open ('student.txt','r') as s:
    for i in s.readlines():
        if word in i:
            print(word, 'found in the file')

        else:
            print(word,'not found in the file')    