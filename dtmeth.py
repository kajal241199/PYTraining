#creating dict to store emp detail
emp = {"CS1201":12400,"CS1203":15600,:CS1205}:12400}
# copy of dictionary
info = emp.copy()
print( info )
# returns dict by extracting given sequence
print( emo.fromkeys("INDIA@20", 1100) )
roll = [1201, 1202, 1203, 1204, 1205]
prize = emp.fromkeys(roll, 500)
print( prize )
#returns value of give key
print( emp.get("CS1203") )
# returns list of tuples(key, value)
print( emp.items() )
#returns list of keys
print( emp.keys() )
#returns list of values
print( emp.values() )
#add new item if given key is not available
emp.update({"CS1202":13500, "CS1206":34500})
print( emp )
#clearing dict
emp.clear()
print( emp )