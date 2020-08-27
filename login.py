import os
import evel
import recogniser
import Say
def login():
    op = 'please enter your username :: '
    Say.Say(op)
    user = input(op)
    op = 'please enter your password :: '
    Say.Say(op)
    pwd = input(op)
    name = evel.evel(pwd)
    path ='database/data/'+str(name)+'/'+str(name)+'.txt'
    try:
        file = open(path,'r')
        r = file.read()
        file.close()
    except:
        dd = 'Username or Password is wrong'
        print(dd)
        Say(dd)
        return False
    acPath = 'database/data/'+str(name)+'/'+'acc'+str(name)+'.txt'
    file = open(acPath,'r')
    det = file.read()
    file.close()
    
    if r == user:
        Say.Say('please wait while we detect your face')
        isuser = recogniser.recognize(user)
        if isuser:
            print('welcome',user)
            st = 'welcome to our system'+str(user)
            Say.Say(st)
            op = 'now you can have access to your account'
            print(op)
            Say.Say(op)
            ap = 'your details are '
            print(ap)
            Say.Say(ap)
            print(det)
        
    else:
        op = 'seems you are not '+str(user)
        print(op)
        Say(op)
        return False
