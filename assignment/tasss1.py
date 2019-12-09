# prg to display employee details
emp = []

for i in range(3):
    an = int(input("enter ac no: "))
    ahn = raw_input("enter ac hname : ")
    ab = float(input("enter ac bal: "))
    #adding into a new list
    emp = [an, ahn, ab]
else:
    for item in range(3):
        print( emp )
