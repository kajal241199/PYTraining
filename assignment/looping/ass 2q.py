#string
str = input("enter a string: ")
print str
vowel = 0
for ch in str:
    if ch in "AEIOUaeiou":
        vowel += 1
        print( ch )
    elif ch in "0123456789":
        digit += 1
        print( digit )
    else:
        word += 1
        print( word )
