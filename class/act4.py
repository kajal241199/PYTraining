class account:
    'to define account class woth account info and operations'

    #creating static/class variables
    bname  = "HDFC BANK"

    def __init__(self):
        'to initialise instance variables'
        account.acstarter += 1
        #declaring/creating instance variables
        self.acno = int(raw_input("enter accont no : "))
        self.acname = raw_input("enter accont h name : ")
        self.acbal = float(raw_input("enter accont blance : "))
        
 
    
    def setaccountinfo(self):
        'to initialise account info'
        #declaring/creating instance variables
        self.acno = int(raw_input("enter accont no : "))
        self.acname = raw_input("enter accont h name : ")
        self.acbal = float(raw_input("enter accont blance : "))
    
    def getaccountinfo(self):
        'to display account detail'
        print("--accont detail--")
        print("ac  no : %d" %self.acno)
        print("ac h name : %s" %self.acname)
        print("ac  balance : %0.2f" %self.acbal)
        print("bankname : %s" %account.bname)

    def withdraw(self, amt):
        'to withdraw the amount fro the account'
        if self.acbal >= amt:
            self.acbal -= amt
            print("balance after withdraw : %0.2frs" %self.acbal)
        else:
            print("insufficient balance")
    
    @staticmethod
    def setbankinfo():
        'to set bank detail'
        account.bname = raw_input("enter bank name : ")
        #creating new static variable
        account.acstarter = raw_input("enter account start no : ")
        print("bank name : %s" %account.bname)
        print("ac start no : %s" %account.acstarter)

    @classmethod
    def setbankdetail(cls, bn, start):
        account.bname = bn
        cls.acstarter = start
        print("bank name : %s" %account.bname)
        print("starter no : %d" %cls.acstarter)

    #invoking implicitly when instance is destroyed
    def __del__(self):
        'to destroy'
        print("bachao, ac no : %d delete ho raha hai" %self.acno)


#creating an object
account.setbankinfo()
account.setbankdetail("icici bank", 7000)
ac1 = account()
ac2 = account()
ac1.getaccountinfo()
ac2.getaccountinfo()
