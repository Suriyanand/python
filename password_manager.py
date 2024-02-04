def add():
    user_name= input("enter your username :")
    user_pass= input("enter your password :")
    with open('user_pass.txt','w') as file:
        file.write(user_name+"|"+user_pass)

def view():
    with open('user_pass.txt','r') as file:
        d=file.readlines()
        print("user_id and password",d)



while(True):
    print("welcome ! back\nTo password Manager ")
    passa=int(input("You have admin password or you forget the password \n 1.I have password \n 2.create new passowrd \n 3.quit\n--->"))
    if passa == 3:
        break
    elif passa == 2:
        passc=input("create a new password :")
        with open('password.txt','w') as file:
            file.write(passc)
            print("password created successfull")
            continue
    elif passa == 1:
        passv=input("please enter yor password :")
        with open('password.txt','r') as file:
            passv = passv.strip()
            if passv in map(str.strip, file):
                choice=int(input("what you want \n1.You can add password\n2.view password\n--->"))
                if choice ==1:
                    print(add())
                else:
                    print(view())





   # passw=input("please enter your admin password :")

