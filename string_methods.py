#string methods
str = "ketan_sharma"
#returns size of given str
size = len(str)
print(size)
#returns an index of given str
print(str.index("k"))
#Checking all chars
print(str.isalnum())
print(str.isalpha())
print("2020".isdigit())
str.replace(" ","-")
print(str.islower())
print(str.isupper())
print(str.capitalize())
print("  ".isspace())
print(str.swapcase())
print(str.count("a"))
tokens = str.split("a")
for items in tokens:
    print(items)
