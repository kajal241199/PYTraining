score = 70
ACT_INFO = [12001, "kajal", 12500.50]
#creating fun to calc cot and maintainence
def cost_main(size):
    'to calc cost and maintainence of flat'
    if size >= 1000:
        rate = 2000
        mrate = 1.0
    else:
        rate = 2500
        mrate = 1.25
    cost = size*rate*1.15
    mamt = size*rate
    print("cost of flat is : %0.2f rs with %0.2f rs maintainence charge " %(cost, mamt) )

def withdrawal(ls, amt):
    'to withdraw from account'
    if ls[2] >= amt:
        ls[2] -= amt
        print("curent balance : %0.2f rs" %ls[2])
    else:
        print("not enough balance")

def deposit(ls, amt):
    'to deposit to account'
    ls[2] += amt
    print("curent balance : %0.2f rs" %ls[2])

def updatescore(value):
    'to update score value'
    global score
    score += value
    print("score is  : %d " %score)
    

#callling functions
cost_main(1200)
updatescore(20)
withdrawal(ACT_INFO, 500)
deposit(ACT_INFO, 500)