with open ('notes.txt','r') as n:
    longest=''
    for i in n.readlines():
        if len(i)>len(longest):
            longest=i


print(longest)