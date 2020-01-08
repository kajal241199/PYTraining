import sys

USER = "admin"
PIN = 1212
print("hello, are you admin?")

def validate():
    'to validate user'
    user = input("enter user name : ")
    pin = int( input("enter pin : "))
    if USER == user and PIN == pin:
        print("welcome, admin you can use basic package")
    else:
        print("invalid user")
        sys.exit(0)

#calling
validate()