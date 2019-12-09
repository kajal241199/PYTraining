# string example
str = "India, Rs@20 #IN"
print( str )
#iterate string
for ch in str:
     print ( ch )
#concatenation
print(str+"india")
#repetetion
print("udpr "*4)
#indexin/slicng/ranging
print( str[7] )
print( str[-11] )
print( str[-10 : -4] ) # from -10 to -5

print( str[4:9] ) # from 4 to 8
print( str[4:] )  #from 4 to end
print( str[:11] ) #from 0 to 10
print( str[-4:] ) #from -4 to -1
print( str[ :-11] ) # from -16 to -11

if"pur" in "jaipur city":
    print("city name")
else:
    print("not a city name")


acno = 22
acname = "kajal singhvi"
acbal = 88.0

txt = "hello  %s,\nU have bal\t%0.2f"%(acname, acbal)
print ( txt )

txt = "hello {2} ,bal is {0} in accoun no {1},".format(acbal,acno,acname)
print ( txt )

