# calculaating call cost
import math

duraton = int(input("entere duration of the call: "))
rate=1.5
mins = math.ceil(duration/60)
cost = mins*rate*1.1
print("call cost is : %0.2f rs with rate of %0.2f rs" %(cost,rate) )
print( type(duration) )
print( type(rate) )