with open ('notes.txt','r') as n:
    data=n.read()

    line=data.splitlines()
    words=data.split()
    char=len(data)

    print("Number of lines:", len(line))
    print("Number of words:", len(words))
    print("Number of characters:", char)

