#creating list to store account details
act = []

for i in range(3):
    an = int(input("enter ac no: "))
    ahn = raw_input("enter ac hname : ")
    ab = float(input("enter ac bal: "))
    #adding into a new list
    info = [an, ahn, ab]
    #appending into act
    act.append(info)
else:
    print( act)
bal = float(raw_input("enter account balance: "))
for item in act:
    if item[2] >= bal:
        print( item )