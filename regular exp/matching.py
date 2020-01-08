import re

str = "cs12345 and cs45678 are topper"
rs = re.match('Cs[0-9]{5}', str, re.I)
if rs:
    print( rs.group() )
else:
    print("match not found")
s = " the cs12345 and cs45678 are topper" # start matching from first word
r = re.match('Cs[0-9]{5}', s, re.I)
if r:
    print( r.group() )
else:
    print("match not found")

mob  = raw_input("enter mobile no : ")
#validating mob no
rs = re.match('^\d{10}$', mob)
if rs:
    print( rs.group(), "valid")
else:
    print("invalid mobile no")