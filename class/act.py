
class account:
    'to define account class woth account info and operations'
    def __init__(self):
        'to initialise instance variables'
        #declaring/creating instance variables
        self.acno = int(raw_input("enter accont no : "))
        self.acname = raw_input("enter accont h name : ")
        self.acbal = float(raw_input("enter accont blance : "))
 
    def __init__(self,an,ahn,ab):
        'to initialise instance variables by args'
        self.acno = an
        self.acname = ahn
        self.acbal = ab
    
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

    def withdrawal(self, amt):
        'to withdraw the amount fro the account'
        if self.acbal >= amt:
            self.acbal -= amt
        print("")

#creating an object
ac1 = account(1234,"kajal",2345)
ac1.getaccountinfo()

ac2 = account(2345,"ishi",5)
ac2.getaccountinfo()
