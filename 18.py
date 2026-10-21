with open ('expense.txt','w') as e:
    total=0
    while True:
        exp_name=input('Enter expense name(exit for stop): ')
        

        if exp_name=='exit':
            print('Exiting')
            break
        exp_amount=int(input("Enter expense amount: "))
        e.write(exp_name+':'+str(exp_amount)+'\n')
        total+=exp_amount


print('Total expense: ',total)