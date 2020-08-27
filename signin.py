import os
import evel
import face_input
import login
import trainer
import Say 

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def signin():
    ip = 'enter your name'
    Say.Say(ip)
    user = input(ip)
    ip = 'enter a password'
    Say.Say(ip)
    pwd= input(ip)
    ip = 'confirm your password'
    Say.Say(ip)
    conf = input(ip)
    ip = 'Enter your details'
    Say.Say(ip)
    acc = input(ip)
    if pwd == conf:
        hval = evel.evel(pwd)
        createFolder('database/data/'+str(hval))
        path = 'database/data/'+str(hval)+'/'+str(hval)+'.txt'
        file = open(path,'w')
        file.write(user)
        file.close()
        acPath = 'database/data/'+str(hval)+'/'+'acc'+str(hval)+'.txt'
        file = open(acPath,'w')
        file.write(acc)
        file.close()
        op = 'wait while we create a database for you'
        print(op)
        Say.Say(op)
        face_input.face_input(user)
        op = 'database is created'
        print(op)
        Say.Say(op)
        trainer.trainer(user)
        op = 'training is done'
        print(op)
        Say.Say(op)
        op = 'would you like to sign in to your account'
        print(op)
        Say.Say(op)
        ans = input('yes / no')
        if ans == 'yes':
            login.login()
        else:
            op = 'thanks for being with us'
            print(op)
            Say.Say(op)
    
