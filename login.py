from fileinput import close


print("1. To Signup")
print("2. To log in")
num = int(input("enter the option: "))
if num== 1:
    username = input("enter the username: ")
    password = input("enter the password: ")
    user = open("user.txt", "w" )
    user.write( username + "\n" + password)
    user.close()
elif num == 2:
    file = open("user.txt", "r")
    logusername = input("enter your username: ")
    logpass = input("enter your password: ")
    fileuser = file.readline()
    filepass = file.readline()
    print(fileuser)
    print(filepass)
    if fileuser == logusername and filepass == logpass:
        print("you are logged in")
    else:
        print("you entered the wrong password")
    file.close()
else:
    print("invalid number")