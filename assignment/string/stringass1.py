p = raw_input("enter a paragraph: ")
digit = 0
symbol = 0
space = 0
alpha = 0
for ch in p:
    if(ch.isdigit()):
        digit += 1
    elif(ch.isalpha()):
        alpha += 1
    elif(ch == " "):
        space += 1
    else:
        symbol += 1
else:
    print("digits = %d, alpha = %d, space = %d, symbol = %d " %(digit,alpha,space,symbol) )

