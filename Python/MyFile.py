def new_file():
    fla=True
    print('----------Directory in txt-------------')
    while fla==True:
        with open('readme.txt','a') as file:
            name1=input('First Name: ')
            name2=input('Last Name: ')
            mail=input('email: ')
            phone=input('phone')
            file.write(name1+ ' '+ name2+ ' '+  mail+ ' '+ phone)
        print('Do you want to continue? (yes/no)')
        var=input('Type "yes" or "no": ')
        if var=='yes':
            fla==True
        else:
            fla==False

new_file()