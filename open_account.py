def openAccount(path):
    file = open(path,'r')
    r = file.read()
    file.close()
    print('you have rupees :: ',r)
    print('to withdraw press 1')
    print('to deposit press 2')
    ip = int(input())
    if ip == 1:
        amt = input('How much :: ')
        if amt<=int(r):
            print(amt,'rupees withdrawn successfully')
            x = int(r)-amt
            file.open(path,'w')
            file.write(str(x))
            file.close
            print('New account balance :: ',x)
        else:
            print('you dont have sufficient money')
    elif ip == 2:
        amt = input('enter the amount :: ')
        file = open(path,'w')
        x = int(r)+amt
        file.write(str(x))
        print('Account updated successfully')
        print('new balance :: ',x)
        file.close()
        
