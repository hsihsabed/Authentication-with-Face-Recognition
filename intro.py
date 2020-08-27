import Say
import login
import signin
def intro():
    st = 'hello and welcome to our system'
    print(st)
    Say.Say(st)
    st = 'to sign in press 1'
    print(st)
    Say.Say(st)
    st = 'to log in press 2'
    print(st)
    Say.Say(st)
    ip = int(input())
    if ip==1:
        signin.signin()
    elif ip==2:
        login.login()

intro()
