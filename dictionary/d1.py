# creating dictionary to store student marks with roll no
marks = {"cs052":12, "cs056":67, "cs047":55}
print( marks )
#iterate dict
for item in marks:
    print ( item, " : ",marks[item] )
#adding new tem
marks["cs088"] = 45
print( marks )
#update an item
marks["cs056"] = 10
print( marks )
#delete an item
del marks["cs052"]
print( marks )
# search value by key
print( marks["cs047"] )
#returns size of dict
print( len(marks) )
#returns str
info = str( marks )
print( info )
print( type(info) )