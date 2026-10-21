file_name=input("Enter file name")

try:
    with open(file_name,'r') as f:
        data=f.read()
        print(data)

except FileNotFoundError:
    print("File not exist")