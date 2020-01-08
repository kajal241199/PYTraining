import re #importing regex module

regex = "[0-9][abcd]pur"
str = "6dpur and 5apur are near but 7epur is far from 3cpur."
#returns  list of all matching tokens
tokens = re.findall(regex, str)
print( tokens )

reno = re.compile("[0-9]+")
txt = "gits since 1999 and 90% placement and 5240 rs avg salary, total 5  degrees and 2020 will be best, finally 101"
#extracting all numbers from given str
numbers = reno.findall(txt)
print( numbers )
#creating regex for roll no
rerollno = re.compile("Cs17\d{3}", re.I)
msg = "cs17405 and Cs17505 are winner but cs1767 and cs17324 are failure but Cs19887 is not valid"
#extracting all rollno no from given stringroll 
roll = rerollno.findall(msg)
print( roll )