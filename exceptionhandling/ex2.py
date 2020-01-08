import datetime 

def getbill(units,rate):
    'to clac bill'
    bill = units*rate*1.1
    print("bill is : %0.2f rs" %bill)

try:
    city = {123:"udr", 345:"jaipur", 122:"bombay"}
    std =int(raw_input("enter std code : "))
    print("%d is std code of %s" %(std, city[std]))
    #callinf function
    getbill(400, 2.5)
    getbill("1", 11)
    fr = open( input("enter file name : ") )
    print( fr.read() )
    fr.close()
except ValueError as ve:
    print("please enter the correct value : ", ve)
except KeyError as ve:
    print("std code is not xisting in dictionary : %d - %s" %(std, ke))
except Exception as ex:
    #craeting/opening file in append mode
    fw = open("error.txt" , "a")
    #returns current date and time
    cdt = datetime.datetime.now()
    fw.write(str(cdt)+"\t"+str(type(ex))+"\t"+str(ex)+"\n")
    fw.close()
print("all is well")
