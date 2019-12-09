# string methods
str = " kajal@24"
size = len(str)
print size
#returns index of given string
print (str.index("k"))
#checking all chars are alphabets and numbers
print( str.isalnum())
# checking all chars are alphabets
print( str.isalpha())
# checking all chars are digits
print( "2020".isdigit())
# replacing space with *
print( str.replace( "k","*"))
# checking all chars are lower case
print( str.islower())
# checking all chars are upper case
print( str.isupper())
# checking if all chars are spaces
print( str.isspace())
print( str.capitalize())
# swaping case
print( str.swapcase())
#returns n of occurances of givn string
print( str.count("k"))
#return list of tokens
token =  str.split("a")
for item in token:
    print( item )