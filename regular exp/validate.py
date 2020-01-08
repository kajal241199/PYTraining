import re

#creating regex to validate roll no
rerollno = re.compile('^(CS|IT)1[4-7]\d{4}$', re.I)

for i in range(2):
    #matchng/validate roll no
    rs = rerollno.match(raw_input("enter roll no : "))
    if rs:
        print("valid")
    else:
        print("invalid")

#creating regex for vehicle no
revno = re.compile('^(G|R)J\d{2}[A-Z]{2}\d{4}$', re.I)

for i in range(2):
    vno = raw_input("enter vehicle no : ")
    #replacing spaces with blanks
    vno = re.sub(" ","", vno)
    rs = revno.match(vno)
    if rs:
        print("valid")
    else:
        print("invalid")