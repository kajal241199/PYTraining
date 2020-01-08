class card:
    'to describe card details'

    card = raw_input("enter a card msg: ")

    def __init__(self):
        'to initialise card info'
        self.cno = int(raw_input("enter card no : "))
        self.chname = raw_input("enter chname : ")
        self.cbal = float(raw_input("enter cbalance : "))
        self.cexdate = raw_input("enter card expiry date : ")
    
    def getcardinfo(self):
        'to display card detail'
        print("c no : %d" %self.cno)
        print("c hname : %s" %self.chname)
        print("c balane : %0.2f" %self.cbal)
        print("c ex date : %s" %self.cexdate)

    def withdraw(self, amt):
        'to withdraw from account balance'
        if self.cbal >= amt:
            self.bal -= amt
            print("current card balane : %0.2f rs" %self.cbal)
        else:
            print("insufficient balance")

#inherting into derived class
class creditcard(card):
    'to describe/represent credit card'

    card = ("enter credit msg : ")

    def __init__(self, cvv):
        'to initialse cvv'
        #calling base class init
        card.__init__(self)
        self.CVV = cvv

    def getcreditcardinfo(self):
        'to display credit card info'
        card.withdraw(self, 10000)
        self.getcardinfo()
        print("CVV = %d" %self.CVV)

    def withdraw(self, amt):
        'to withdraw from credit limit by cvv'
        if self.cbal >= amt and self.CVV == cvv:
            self.cbal -= amt
            print("current credt balance : %0.2f rs" %self.cbal)
        else:
            print("low balance")

cd1 = creditcard(123)
cd1.getcreditcardinfo()
cd1.withdraw(10000)