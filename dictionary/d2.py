#creating dict to store account details
ACT = {}
for i in range(2):
    an = int(raw_input("enter ac no : "))
    ahn = raw_input("enter hname : ")
    ab = float(raw_input("enter ac balance : "))
    pin = int(raw_input("enter ac pin : "))
    # adding account info into dict
    ACT[an] = [ahn, ab, pin]
else:
    print( ACT )
#defining fun
def withdraw(an,amt):
    'to withdraw the amount'
    if an in ACT:
        pn = int(raw_input("enter pin no: "))
        if ACT[an][1] >= amt and ACT[an][2]==pn:
            ACT[an][1] -= amt
            print("bal : %0.2f rs" %ACT[an][1])
        else:
            print("wrong pin or low balance")
    else:
        print("acconut no is not available")

def deposit(an,amt):
    'to withdraw the amount'
    if an in ACT:
        pn = int(raw_input("enter pin no: "))
        if ACT[an][2]==pn:
            ACT[an][1] += amt
            print("bal : %0.2f rs" %ACT[an][1])
        else:
            print("wrong pin")
    else:
        print("acconut no is not available")
    
#fun call
withdraw(1203, 1200)
deposit(1203, 1200)