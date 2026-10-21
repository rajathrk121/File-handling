import os

file_n=input("Enter file name: ")

if os.path.exists(file_n):
    with open (file_n,'r') as f:
        data=f.read()

        print(data)

else:
    print("File not exist")