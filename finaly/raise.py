#creating exception class
class NegativeValueError(RuntimeError):
    'to represent negative value error'

    def __init__(self, msg):
        'to initialise a msg'
        self.msg = msg

    def __str__(self):
        return self.msg

def get_bill(units):
        'to calculate electricity bil'
        if units<0:
            #creating exception
            nve = NegativeValueError("please enter positive value")
            #raising an exception
            raise nve
        if units>=500:
            rate = 5.5
        else:
            rate = 1.1
        bill = rate*units*2.2
        print("pay bill is : %0.2f rs" %bill)

try:
    units = int(raw_input("enter inputs: "))
    #calling function
    get_bill(units)
    get_bill(-400)
    print("everything is fine")
except Exception as ex:
    print(type(ex), " : ", ex)
print("all is well")