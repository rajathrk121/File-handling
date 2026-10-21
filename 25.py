def add_n():
    note=input("Enter note: ")

    with open ('note.txt','a')as n:
        n.write(note+'\n')


def view_n():
    try :
        with open ('note.txt','r') as n:
        
            data=n.read()
            print(data)
    except FileNotFoundError:
        print("File not found")

def search_n():
    note=input("Enter note: ")
    found=False
    try:
        with open("note.txt",'r') as n:
            data=n.read()
            notes=data.splitlines()

            for item in notes:
                if note == item:
                    print(item)
                    found = True
                    break
        if not found:
            print(note,'not found')

    except FileNotFoundError:
        print("File not found")

def stop():
    print('Exiting')
    exit()


while True:
    choice=input("Enter your choice(add_note/view_note/search_note/exit)")

    match choice:
        case 'add_note':
            add_n()

        case 'view_note':
            view_n()
        case 'search_note':
            search_n()
        case 'exit':
            stop()
            
        case _:
            print("Enter a valid choice")




                

