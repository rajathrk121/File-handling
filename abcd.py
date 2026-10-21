with open ('sample.txt','w+') as a:
    a.write('Python is easy')
    a.seek(0)

    b=a.read()
    print(b)