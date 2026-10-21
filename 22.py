file_n=input("Enter file name: ")

try:
    with open(file_n,'r') as f:
        data=f.read()
        print(data)

except FileNotFoundError:
    print("File not exist")

except OSError:
    print("An error occured while reading the file")