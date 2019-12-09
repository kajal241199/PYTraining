#string
str = raw_input("enter a string: ")
print str
vowel = 0
digit = 0
word = 0
for ch in str:
    if ch in "AEIOUaeiou":
        vowel += 1
    elif ch in "0123456789":
        digit += 1
    elif ch in split()
        word += 1
print(" vowels =%d digit =%d word =%d" %(vowel,digit,word) )